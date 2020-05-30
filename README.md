# Train Machine Learning model by integrating it with git, github, docker and jenkins
In this project i am going to train ML model by integrating it with git, github, docker and jenkins. If the model doesn't get the desired accuracy jenkins will tweak the model and again train it and this process will be repeated untill get the desired accuracy.

## Work to be done in this project
1. Create a docker container image that has Python3, tensorflow, Keras installed using dockerfile
2. Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins 
3. Job1: Pull the Github repository automatically when some developer push code to Github
4. Job2: By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter image container to deploy code and start training( e.g. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the CNN processing)
5. Job3: Train model and predict accuracy
6. Job4: If accuracy is less than 80% , then tweak the machine learning model architecture and retrain it
7. Job5: Notify that the desired accuracy model is created
8. Job6: If the container where model is training, fails due to any reason then this job should automatically start the respective container

## Let's see the step by step process
