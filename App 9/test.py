import cv2

def main():
    cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    print("Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
