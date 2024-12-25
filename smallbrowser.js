// smallbrowser.js
const smallbrowser = {
    open: function(url, options = {}) {
        const { width = 800, height = 600, resizable = true } = options; // Destructure the options object to get width, height, and resizable.

        // Create a string of options for the window
        const optionsString = `width=${width},height=${height},resizable=${resizable ? 'yes' : 'no'}`;
        
        // Use window.open to open the URL with the specified options
        window.open(url, "SmallBrowser", optionsString);
    }
};
