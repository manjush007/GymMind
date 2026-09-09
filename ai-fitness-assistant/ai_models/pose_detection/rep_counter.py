import math

def calculate_angle(a, b, c):
    """Calculate the angle between three points: a, b (vertex), and c."""
    a = [a['x'], a['y']]
    b = [b['x'], b['y']]
    c = [c['x'], c['y']]
    
    radians = math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0])
    angle = math.degrees(radians)
    
    if angle < 0:
        angle += 360
        
    return angle

class RepCounter:
    def __init__(self):
        self.counter = 0
        self.stage = None # "down" or "up"

    def update_squat(self, landmarks):
        """
        Calculates squat reps using hip, knee, and ankle angles.
        MediaPipe landmark mapping:
        23, 24 = left/right hip
        25, 26 = left/right knee
        27, 28 = left/right ankle
        """
        if len(landmarks) < 29:
            return self.counter
            
        # Get coords for left leg (can average both legs for robustness)
        hip = landmarks[23]
        knee = landmarks[25]
        ankle = landmarks[27]
        
        # Check visibility
        if knee["visibility"] < 0.5 or hip["visibility"] < 0.5:
            return self.counter

        angle = calculate_angle(hip, knee, ankle)

        # Basic squat threshold logic (angles vary based on camera angle, these are approximations)
        if angle > 160: # Standing standing
            if self.stage == "down":
                self.counter += 1
                self.stage = "up"
        if angle < 90: # Squatting down
            self.stage = "down"
            
        return self.counter

    def get_count(self):
        return self.counter
