pipeline{
    agent { label jenkins-agent };
   
    stages{
        stage("clone repo"){
            steps{
            git url: "https://github.com/meghraj8788/docker_2.0.git", branch: "master"
        }
        }
        stage("build image"){
            steps{
                dir('java-app') {
                sh "docker build -t meghrajfand8788/java-app:latest ."
                }
            }
        }
        stage("uplode image to hub"){
            steps{
                withCredentials([usernamePassword(
                    credentialsId : "hubtoken",
                    passwordVariable: "dockerpass",
                    usernameVariable : "dockeruser"
                    )]){
                sh "docker login -u ${env.dockeruser} -p ${env.dockerpass}"
                dir('java-app') {
                sh "docker push ${env.dockeruser}/java-app:latest"
                }
                    }
                }
        }
        stage("compose file run"){
            steps{
                dir('java-app') {
                sh "docker compose up -d"
                }
            }
        }
    }
}
