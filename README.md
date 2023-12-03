# Vendor Manager Application

The Vendor Manager Application is a Django-based system developed using Django and Django REST Framework to manage vendor-related activities, such as vendor performance evaluation, purchase order tracking, and more.

## Functionalities

- **Vendor Performance Evaluation**: Allows users to evaluate vendor performance based on metrics like on-time delivery rate, quality rating average, response time, and fulfillment rate.
- **Purchase Order Tracking**: Tracks and manages purchase orders with acknowledgment, completion, and status tracking features.
- **Efficient Calculations**: Optimized logic for calculating metrics and processing data efficiently.
- **Real-time Updates**: Utilizes Django signals for real-time updates upon changes in purchase order data.

## Installation and Setup

Follow these steps to set up and run the project locally:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/your-username/vendor-manager.git
    cd vendor-manager
    ```

2. **Create a Virtual Environment (Optional but Recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # For Linux/Mac
    venv\Scripts\activate     # For Windows
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run Migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Start the Development Server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the Application:**

    Open your web browser and go to http://localhost:8000/ to access the Vendor Manager Application.

## Usage

Describe how to use the application here, including API endpoints, admin panel access, and any other relevant details.

## Contributing

If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
