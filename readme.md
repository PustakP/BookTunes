# BookTunes 📚🎶

Reading by yourself ever feel a bit too quiet? BookTunes is here to help you out with a personalized playlist made especially for your book (and you ❤️).

## What is BookTunes?

BookTunes is a web application that generates song recommendations based on the vibe of the book you're currently reading. It creates a unique playlist to enhance your reading experience.

## How it Works

BookTunes uses OpenAI's GPT-3.5 Turbo model to generate song recommendations. Simply enter the name of your book, and BookTunes will create a playlist tailored to the mood of the book.

## Getting Started

To use BookTunes, you need to set up the following credentials:

- OpenAI API Key
- Spotify Client ID and Client Secret

Make sure to set these credentials as environment variables:
```bash
export OPNAI=your_openai_api_key
export cid=your_spotify_client_id
export csecret=your_spotify_client_secret
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/BookTunes.git
cd BookTunes
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python your_app_file.py
```

4. Open your browser and go to [http://localhost:8080](http://localhost:8080)

## Usage

1. Enter the name of the book you're reading.
2. Click on the "Generate Playlist" button to get personalized song recommendations.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or find any issues, please open an [issue](https://github.com/your-username/BookTunes/issues) or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

Happy Reading and Happy Listening! 📖🎧
```

Feel free to customize it further based on your preferences and additional information about your project!
