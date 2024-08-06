# Dorky

This project is a Dockerized service that checks if your domain appears in Google Dorks. If it does, it sends an email notification. The service fetches the latest Google Hacking Database (GHDB) entries, checks them against your domain, and notifies you if any dorks are found.

## Features

- Fetches the latest Google Hacking Database (GHDB) entries.
- Checks if your domain appears in the dorks.
- Sends an email notification if any dorks are found.
- Runs as a Docker container.

## Setup

### Prerequisites

- Docker
- Python 3.9+
- A valid SMTP server for sending emails

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/aguspatur22/dorky.git
   cd dorky
   ```

2. **Create a .env file:**
   ```sh
   touch .env
   ```

   Add the following content to the .env file:
   ```sh
   DOMAIN=yourdomain.com
   ```

3. **Build the Docker image:**
   ```sh
   docker build -t dorky .
   ```

4. **Run the Docker container:**
   ```sh
   docker run -d --name dorky-checker dorky
   ```


## Configuration

- DOMAIN: The domain you want to check against Google Dorks.

## File Structure

- main.py: The main entry point of the application.
- fetcher.py: Fetches the latest GHDB entries.
- parser.py: Parses the GHDB XML content.
- checker.py: Checks if the domain appears in the dorks.
- notifier.py: Sends email notifications.
- requirements.txt: Lists the Python dependencies.
- Dockerfile: Docker configuration file.
- .env: Environment variables file

## Example

To manually run the service, execute: 
   ```sh
   docker run --rm dorky
   ```


## Setting Up as a Cronjob in Linux

To set up the Docker container to run as a cronjob once a day, follow these steps:

1. **Open the crontab file:**
   ```sh
   crontab -e
   ```

2. **Add the following line to schedule the job to run daily at midnight:**
   ```sh
   0 0 * * * docker run --rm dorky
   ```

3. **Save and exit the crontab editor.**

The cronjob will now run the Docker container daily, checking for Google Dorks and sending email notifications if any are found.


## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.