from controllers.user_controller import UserController
from utils.logger import Logger

def main():
    """
    The main entry point of the application.

    This function initializes the logger, logs the application startup, 
    creates an instance of the UserController, starts the controller, 
    and logs the application termination.
    """
    Logger()  # Initialize the logger
    Logger.log_info("Application started.")
    
    # Initialize and start the user controller
    user_controller = UserController()
    user_controller.start()
    
    # Log the termination of the application
    Logger.log_info("Application terminated.")

if __name__ == "__main__":
    main()
