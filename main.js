const { app, BrowserWindow } = require("electron");

function createWindow() {
    const win = new BrowserWindow({
        width: 1200,
        height: 700,
        webPreferences: {
            nodeIntegration: true
        }
    });

    win.loadFile("Frontend/index.html");
}

app.whenReady().then(createWindow);