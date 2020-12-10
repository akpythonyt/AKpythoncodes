import face_recognition
knownimage=face_recognition.load_image_file("/home/arun/Pictures/Known images/Elonmusk.jpeg")
unknownimage=face_recognition.load_image_file("/home/arun/Pictures/Known images/Elonmusk.jpeg")

knowencoding=face_recognition.face_encodings(knownimage)[0]
unknownencoding=face_recognition.face_encodings(unknownimage)[0]

results=face_recognition.compare_faces([knowencoding],unknownencoding)
if results[0]==True:
   print("Image Matched Successfully")
else:
   print("Image Mismatched")
