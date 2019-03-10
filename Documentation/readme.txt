Welcome to David's homework.

I. Setting up environment:
    1. Navigate to Scripts(folder) and use "activate" command. (now you're running virtualenv)
II. Run solutions:
    1. Navigate to Solutions.
    2. For running task one solution, please enter: python Task_1.py (or Task_1_b.py or Task_1_c.py) #Note: More and more complex.
    3. For running task two solution, please enter: python Task_2.py
    4. The csv file (results.csv) will be re-generated every time task two is called.


Docker:
    docker build -t homework
    docker run -d -it homework
    docker ps -a
    (copy homework's container id)
    docker exec -it CONTAINERID bash
