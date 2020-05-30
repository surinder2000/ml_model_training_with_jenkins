# Train Machine Learning model by integrating it with git, github, docker and jenkins
In this project i am going to train ML model by integrating it with git, github, docker and jenkins. If the model doesn't get the desired accuracy jenkins will tweak the model and again train it and this process will be repeated untill get the desired accuracy.

## Work to be done in this project
1. Create a docker container image that has Python3, tensorflow, Keras installed using dockerfile
2. Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins 
3. Job1: Pull the Github repository automatically when some developer push code to Github
4. Job2: By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter image container to deploy code and start training( e.g. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the CNN processing)
5. Job3: Train model and predict accuracy
6. Job4: If accuracy is less than 80% , then tweak the machine learning model architecture and retrain it
7. Job5: Push code to Github master branch and notify that the desired accuracy model is created
8. Job6: If the container where model is training, fails due to any reason then this job should automatically start the respective container

## Let's see the step by step process
### 1. Create a docker container image that has Python3, tensorflow, Keras installed using dockerfile
* The following is the code of the Dockerfile

![Dockerfile code](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/Dockerfilecode.png)

* To build image from Dockerfile use the follwing command
               
      docker build -t image_name:version path
      e.g docker build -t tensorflow_cpu:v1 .  (Here . means current directory)
      
   [Link to Docker image!](https://hub.docker.com/repository/docker/surinder2000/tensorflow_cpu) 
   
### 2. Let's create Jenkins jobs
#### Job 1: Pull the Github repository automatically when some developer push code to Github
* In Source Control Management section put the Github repository url and branch name

![Git configuration](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job11.png)

* In Build trigger section select Poll SCM for checking the github repository every minute

![Build trigger](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job12.png)

* In the Build section from Add build step select Execute shell and put the following code in the command box

![Execute shell](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job13.png)

* Click on Apply and Save

#### Job2: By looking at the code or program file, Jenkins should automatically start the respective machine learning software installed interpreter image container to deploy code and start training( e.g. If code uses CNN, then Jenkins should start the container that has already installed all the softwares required for the CNN processing)
* In Build trigger section select Build after other projects are built and put job name **Pull data from github** in the Project to watch box and check Trigger only if build is stable

![Build trigger](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job21.png)

* In the Build section from Add build step select Execute shell and put the following code in the command box

![Execute shell](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job22.png)

* Click on Apply and Save

#### Job3: Train model and predict accuracy
* In Build trigger section select Build after other projects are built and put job name **Check code** in the Project to watch box and check Trigger only if build is stable

![Build trigger](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job31.png)

* In the Build section from Add build step select Execute shell and put the following code in the command box

![Execute shell](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job32.png)

* Click on Apply and Save

#### Job4: If accuracy is less than 80% , then tweak the machine learning model architecture and retrain it
* In Build trigger section select Build after other projects are built and put job name **Train model and get accuracy** in the Project to watch box and check Trigger only if build is stable

![Build trigger](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job41.png)

* In the Build section from Add build step select Execute shell and put the following code in the command box

![Execute shell](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job42.png)

* Click on Apply and Save

#### Job5: Push code to Github master branch and notify that the desired accuracy model is created
* In Source Control Management section put the Github repository url and branch name

![Git configuration](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job51.png)

* In Build trigger section select Trigger builds remotely and give Authentication token and also select Build after other projects are built and put job name **Tweak model** in the Project to watch box and check Trigger only if build is stable

![Build trigger](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job52.png)

* In the Build section from Add build step select Execute shell and put the following code in the command box

![Execute shell](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job53.png)

* In the Post-build Actions section select Git publisher and check Push Only if Build Succeeds and click on Add Branch put **master** in Branch to push and **origin** in Target remote name

![Post-build Push](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job54.png)

* In the Post-build Actions section select Editable Email notification and put the email address of developer, subject and message content (Note: We need to configure SMTP server for sending mail. For this go to Manage jenkins -> Configure -> Extended Email notification and put the details there) 

![Post-build Email](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job55.png)

* Click on Apply and Save

#### Job6: If the container where model is training, fails due to any reason then this job should automatically start the respective container
* In Build trigger section select Build after other projects are built and put job names **Code check, Monitor the model training container** in the Project to watch box and check Trigger only if build is stable

![Build trigger](https://github.com/surinder2000/ml_model_training_with_jenkins/b0lob/master/job61.png)

* In the Build section from Add build step select Execute shell and put the following code in the command box

![Execute shell](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/job62.png)

* Click on Apply and Save

That's all our setup is ready

Now as soon as the developer commit new ML model in the developer repository it will get automatically pulled by the jenkins job, jenkins job check the model whether it is regression model or neural network model and accordingly launch the respective docker image for training the model, for example if the model is neural network model then jenkins launch the docker images that has tensorflow, keras installed in it. After launching the container jenkins job start the model training and when model gets trained jenkins job check the accuracy of the model if it the desired accuracy is achieved then jenkins job will send email to developer else jenkins job tweak the model and retrain it untill get the desired accuracy.

![Email screenshot](https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/mailshot.png)

Following is the build pipeline view of the Jenkins jobs

![Build Pipeline view]!(https://github.com/surinder2000/ml_model_training_with_jenkins/blob/master/buildpipelineview.png)

