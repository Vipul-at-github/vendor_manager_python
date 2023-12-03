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

## API Endpoints Usage

The API provides various endpoints to interact with the application's resources:

- **GET `/api/vendors/`**: Retrieve a list of all vendors.
- **GET `/api/vendors/{vendor_id}/performance/`**: Fetch performance metrics for a specific vendor.
- **GET `/api/purchase_orders/`**: Retrieve a list of all orders purchased.
- **POST `/api/purchase_orders/{po_id}/acknowledge/`**: Acknowledge a purchase order.

## Accessing Admin Panel

1. Run the development server.
2. Go to `http://localhost:8000/admin/` in your browser.
3. Log in with admin credentials.
4. Manage vendors, purchase orders, and other related data from the admin panel.

## Swagger API Documentation

- Access API documentation at `http://localhost:8000/api/docs/swagger/`.
- Explore and test API endpoints using the Swagger UI interface.

## Additional Information

For more details or any issues, contact: manevip17@gmail.com.
## Contributing

If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
