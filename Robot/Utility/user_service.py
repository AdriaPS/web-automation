class UserService:
    def __init__(self, logger, file_path):
        self.logger = logger
        self.file_path = file_path
        
        self.logger.info("User Service constructor")
        
    def get_user_data(self):
        self.logger.info("Started getting data from the users file.")
        user_data = []        
        f = open(self.file_path, "r")
        
        with open(self.file_path) as f:
            for i, line in enumerate(f, 1):
                variables = line.strip().split(",")
        
                if len(variables) < 2:
                    self.logger.error(f"There aren't enough variables to process the line {i}.")
                    continue
                elif len(variables) > 2:
                    self.logger.error(f"There are too many variables to process the line {i}.")
                    continue
        
                username, access_key = variables
        
                data = {
                }
        
                user_data.append(data)