pipeline {
    agent any
    environment {
        MAX_LIMIT = 25
        MIN_LIMIT = 10
    }
    stages {
        stage('Generate Log') {
            steps {
                script {
                    // Simulating a step that logs values, e.g., from a sensor or calculation
                    echo "Value: 50"
                    echo "Value: 120" // This is out of limit (greater than MAX_LIMIT)
                    echo "Value: 5"   // This is out of limit (less than MIN_LIMIT)
                }
            }
        }
        stage('Check Log for Out-of-Limit Values') {
            steps {
                script {
                    // Read the logs of the current build
                    def log = currentBuild.rawBuild.getLog(1000) // Reads up to 1000 lines

                    // Define a pattern to extract values from the logs
                    def pattern = ~/Value: (\d+)/

                    // Iterate over each line in the log
                    log.each { line ->
                        def matcher = (line =~ pattern)
                        if (matcher.matches()) {
                            // Extract the value and convert it to an integer
                            int value = Integer.valueOf(matcher[0][1].intValue()

                            // Check if the value is out of the specified limits
                            if (value > env.MAX_LIMIT || value < env.MIN_LIMIT) {
                                echo "ALERT: Value ${value} is out of limits!"
                                // You can mark the build as unstable, or fail it based on requirements
                                currentBuild.result = 'UNSTABLE'
                            }
                        }
                    }
                }
            }
        }
    }
}
