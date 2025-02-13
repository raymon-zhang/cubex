html = "<div class='grid'> <div class='viz'> <div class='cube' id='cube' style='width:100%; height:80%'></div> </div> <div class='timer'>timer</div> <div class='scan'></div> <div class='solve'></div></div>"
css = """
    body {
        background-color: #282828;
    }

    #c3 {
        display: block;
        padding: 0;
        height: 100vh;
        width: 100vw;
    }

    #c4 {
        display: grid;
        place-items: center;
        height: 100vh;
        width: 100vw;
    }

    .grid {
        grid-template-columns: repeat(6, 1fr);
        grid-template-rows: 5fr 2fr;
        grid-gap: 35px;
        width: 60vw;
        height: 80vh
    }

    .grid > div {
        background-color: #444444;
        padding: 50px 50px;
        border-radius: 20px;
        box-shadow: 0px 20px 20px -5px #070707, inset 0px 3px 0.5px -1.5px #878787, inset 3px 0px 0.5px -1.5px #141414, inset -3px 0px 0.5px -1.5px #141414, inset 0px -3px 0.5px -1.5px #2e1818;
    }

    .viz {
        grid-column: span 4;
    }

    .timer {
        grid-column: span 2;
    }

    .scan, .solve {
        grid-column: span 3;
        display: grid;
        place-items: center;
    }

    button.bg-primary {
        width: 100% !important;
        border-radius: 1000px !important;
        font-size: 20pt !important;
        font-weight: bold !important;
        font-family: Jost !important;
        background: linear-gradient(#f4c9ab, #e67849) !important;
        text-shadow: 0px 2px 1px #9A4B3C;
        box-shadow: 0px 10px 20px -5px #9A4B3C, 0px 10px 20px 0px #070707 !important;
    }

    .cube {
        display: inline-block;
    }
"""
