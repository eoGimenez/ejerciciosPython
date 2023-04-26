import cv2
import face_recognition as freco

control_img = freco.load_image_file('FotoA.jpg')
test_img = freco.load_image_file('FotoB.jpg')

control_img = cv2.cvtColor(control_img, cv2.COLOR_BGR2RGB)
test_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2RGB)

face_place_a = freco.face_locations(control_img)[0]
codificated_face_a = freco.face_encodings(control_img)[0]
face_place_b = freco.face_locations(test_img)[0]
codificated_face_b = freco.face_encodings(test_img)[0]

cv2.rectangle(control_img,
              (face_place_a[3], face_place_a[0]),
              (face_place_a[1], face_place_a[2]),
              (0, 255, 0),
              2)
cv2.rectangle(test_img,
              (face_place_b[3], face_place_b[0]),
              (face_place_b[1], face_place_b[2]),
              (0, 255, 0),
              2)


# el tercer valor de compare_faces es la distancia
result = freco.compare_faces([codificated_face_a], codificated_face_b)
distance = freco.face_distance([codificated_face_a], codificated_face_b)

cv2.putText(test_img,
            f'{result[0]} - {distance[0].round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2)


cv2.imshow('Foto Control', control_img)
cv2.imshow('Foto Prueba', test_img)

cv2.waitKey(0)
