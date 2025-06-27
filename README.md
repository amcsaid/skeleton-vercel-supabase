# Supabase FastAPI Vercel Application

This is a minimal FastAPI application that connects to a Supabase table and is ready for Vercel deployment.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd supabase_fastapi_vercel
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up Supabase:**
    *   Create a Supabase project at [supabase.com](https://supabase.com/).
    *   In your Supabase project, create a table named `users` with the following columns:
        *   `id`: `INT8` (Primary Key)
        *   `name`: `TEXT`
    *   Add some sample data to the `users` table.

5.  **Configure Supabase credentials:**
    *   Rename the `.env.example` file to `.env` (if you create one later, or directly edit .env).
    *   Update the `.env` file with your Supabase project URL and anon key:
        ```env
        SUPABASE_URL="your_supabase_url"
        SUPABASE_KEY="your_supabase_anon_key"
        ```

6.  **Run the application locally:**
    ```bash
    uvicorn main:app --reload
    ```
    The application will be available at `http://127.0.0.1:8000`. You can access the endpoint at `http://127.0.0.1:8000/items`.

## Deployment to Vercel

1.  **Sign up or log in to Vercel.**
2.  **Import your Git repository.**
3.  **Configure the project:**
    *   Vercel should automatically detect it as a Python project.
    *   Ensure the build command and output directory are configured correctly (usually auto-detected).
    *   Add your Supabase URL and Key as environment variables in the Vercel project settings.
4.  **Deploy.**

## API Endpoint

*   `GET /items`: Retrieves a list of users from the Supabase `users` table.
