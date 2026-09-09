import cv2
import mediapipe as mp

class PoseDetector:
    def __init__(self, static_image_mode=False, model_complexity=1,
                 smooth_landmarks=True, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(static_image_mode=static_image_mode,
                                      model_complexity=model_complexity,
                                      smooth_landmarks=smooth_landmarks,
                                      min_detection_confidence=min_detection_confidence,
                                      min_tracking_confidence=min_tracking_confidence)
        self.mp_draw = mp.solutions.drawing_utils

    def find_pose(self, img, draw=True):
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)
        if self.results.pose_landmarks and draw:
            self.mp_draw.draw_landmarks(img, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
        return img

    def get_landmarks(self, img, draw=True):
        """Returns a list of dicts mapping id to (x, y) coordinates"""
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append({"id": id, "x": cx, "y": cy, "z": lm.z, "visibility": lm.visibility})
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return lmList
