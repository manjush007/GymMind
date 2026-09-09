def analyze_posture(landmarks):
    """
    Very basic posture analysis comparing shoulder and hip alignment.
    Returns a score from 0-100 indicating upright posture.
    """
    if len(landmarks) < 25:
        return 100
        
    left_shoulder = landmarks[11]
    right_shoulder = landmarks[12]
    left_hip = landmarks[23]
    right_hip = landmarks[24]
    
    # Calculate shoulder midpoint
    shoulder_mid_x = (left_shoulder['x'] + right_shoulder['x']) / 2
    
    # Calculate hip midpoint
    hip_mid_x = (left_hip['x'] + right_hip['x']) / 2
    
    # Deviation in X axis (assuming lateral camera view for certain exercises etc)
    # Ideally for upright posture, shoulder midpoint x approx == hip midpoint x.
    # This is a highly simplified heuristic and depends massively on camera angle.
    
    deviation = abs(shoulder_mid_x - hip_mid_x)
    
    # Convert deviation to a 0-100 score (100 is perfectly aligned)
    # Assuming max acceptable deviation is 50 pixels (arbitrary without knowing image res)
    score = max(0, 100 - (deviation * 2))
    
    return int(score)
