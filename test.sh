#./darknet detector test cfg/imgrec.data cfg/yolo-imgrec-test.cfg yolo-imgrec.backup $1 -out predict -thresh 0.1 -gpus 1
./darknet detector test cfg/new_images.data cfg/new_images_test.cfg new_images.backup $1 -out $2 -thresh 0.5 -gpus 1

