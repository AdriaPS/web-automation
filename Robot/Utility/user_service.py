class UserService:
    def __init__(self, logger, file_path):
        self.logger = logger
        self.file_path = file_path
        
        self.logger.info("User Service constructor")
        
    # Function to get the data from a .txt file.
    def get_user_data(self):
        self.logger.info("Started getting data from the users file.")
        user_data = []        
        f = open(self.file_path, "r")
        
        # Open the .txt file.
        with open(self.file_path) as f:
            # Iterate through each line to get the data from multiple users, also use enumerate to track the lines
            # so it can be stored in the Log to check which user failed.
            for i, line in enumerate(f, 1):
                variables = line.strip().split(",")
        
                # Strip the variables from the .txt file, in this case I just want username and password, if the line
                # has more or less variables, I log an error and continue with the next line of the file.
                if len(variables) < 2:
                    self.logger.error(f"There aren't enough variables to process the line {i}.")
                    continue
                elif len(variables) > 2:
                    self.logger.error(f"There are too many variables to process the line {i}.")
                    continue
        
                username, password = variables
        
                # The user is stored as a data dictionary so it's easier to get the information later for the log in.
                data = {
                    "username":username,
                    "password":password
                }
                user_data.append(data)
                
        return user_data