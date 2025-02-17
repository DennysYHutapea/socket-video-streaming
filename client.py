import socket
import cv2
import pickle
import struct
import imutils

def run():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host_ip = "192.168.229.179"
    port = 10050

    client_socket.connect((host_ip, port))
    data = b""
    payload_size = struct.calcsize("Q")

    while True:
        while (len(data)) < payload_size:
            packet = client_socket.recv(4*1024)
            if packet: 
                data += packet
            else:
                break
        
        packed_msg_size = data[:payload_size]
        data = data[payload_size:]
        msg_size = struct.unpack("Q", packed_msg_size)[0]

        while len(data) < msg_size:
            data += client_socket.recv(4*1024)
        
        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame = pickle.loads(frame_data)
        cv2.imshow("receiving...", frame)
        key = cv2.waitKey(10)
        if key == 13:
            break

        client_socket.close()


if __name__ == "__main__":
    run()