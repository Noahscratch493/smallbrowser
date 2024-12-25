# SmallBrowser - A Lightweight Browser that You Can Open in Your Browser!

SmallBrowser is a simple, lightweight browser utility that allows you to open websites in a customizable, small pop-up window with adjustable properties. It's perfect for quickly viewing content without navigating away from your main page.

## Features

- **Customizable window size**: Set the width and height of the browser window.
- **Resizable option**: Make the window resizable or fixed.
- **Lightweight**: Designed to be simple and efficient with minimal setup.

## Installation

To use SmallBrowser in your web project, simply import the `smallbrowser.js` file and include it in your HTML or JavaScript project.

### Steps:

1. Open your HTML Editor and paste this code:

    ```html
   <script src="https://noahscratch493.github.io/smallbrowser/smallbrowser.js"></script>
   ```


2. **Call the `smallbrowser.open()` function** in your code with the desired URL and options.

### Example HTML:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Small Browser Example</title>
    <script src="https://noahscratch493.github.io/smallbrowser/smallbrowser.js"></script>
</head>
<body>
    <button onclick="smallbrowser.open('https://www.google.com', { width: 1024, height: 768 })">
        Open Google in Small Browser
    </button>
</body>
</html>
```

### Example Usage:

```javascript
// Open Google with customized window size
smallbrowser.open('https://www.google.com', { width: 1024, height: 768, resizable: true });
```

## API

### `smallbrowser.open(url, options)`

- **url**: The URL of the site you want to open in the small browser window (string, required).
- **options**: An optional object to configure the window's properties.
  - **width**: Width of the window (default: `800`).
  - **height**: Height of the window (default: `600`).
  - **resizable**: Set to `true` to make the window resizable, or `false` to make it fixed (default: `true`).

### Example:

```javascript
smallbrowser.open("https://www.example.com", { width: 1024, height: 768, resizable: false });
```

This will open "https://www.example.com" in a fixed-size window of 1024px by 768px.

## Customization

You can customize the window options (width, height, resizable) by passing an object to the `smallbrowser.open()` function. Here’s a quick reference for the options:

```javascript
{
  width: 1024,      // Set custom width (default: 800)
  height: 768,      // Set custom height (default: 600)
  resizable: true   // Make the window resizable (default: true)
}
```

## Compatibility

- Works on most modern browsers (Chrome, Firefox, Safari, Edge).
- Pop-up blockers might block the window in some browsers, so ensure pop-ups are allowed for this to work.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
