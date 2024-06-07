from flask import Flask, request
#from origin import origin
app = Flask(__name__)

@app.route('/hi')
def hello_world():
    return 'Successful response.'

@app.route('/')
def svg_endpoint():
    type = request.args.get('type')
    text1 = request.args.get('text1')
    text2 = request.args.get('text2')
    height = request.args.get('height')
    width = request.args.get('width')

    # Assuming you have an svgs dictionary with different SVG templates
    svgs = {
        "origin": lambda text1, text2, height, width: f"""<svg fill="none" viewBox="0 0 {width} {height}" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
	<foreignObject width="100%" height="100%">
		<div xmlns="http://www.w3.org/1999/xhtml">
			<style>
				@keyframes rotate {{
					0% {{
						transform: rotate(3deg);
                    }}
					100% {{
						transform: rotate(-3deg);
                    }}
				}}

				@keyframes gradientBackground {{
					0% {{
						background-position: 0% 50%;
					}}
					50% {{
						background-position: 100% 50%;
					}}
					100% {{
						background-position: 0% 50%;
					}}
				}}

				@keyframes fadeIn {{
					0% {{
						opacity: 0;
					}}
					66% {{
						opacity: 0;
					}}
					100% {{
						opacity: 1;
					}}
				}}

				.container {{
					font-family:
						system-ui,
						-apple-system,
						'Segoe UI',
						Roboto,
						Helvetica,
						Arial,
						sans-serif,
						'Apple Color Emoji',
						'Segoe UI Emoji';
					display: flex;
					flex-direction: column;
					align-items: center;
					justify-content: center;
					margin: 0;
					width: 100%;
					height: {height}px;
					background: linear-gradient(-45deg, #fc5c7d, #6a82fb, #05dfd7);
					background-size: 600% 400%;
					animation: gradientBackground 10s ease infinite;
					border-radius: 10px;
					color: white;
					text-align: center;
				}}

				h1 {{
					font-size: 50px;
					line-height: 1.3;
					letter-spacing: 5px;
					text-transform: uppercase;
					text-shadow:
						0 1px 0 #efefef,
						0 2px 0 #efefef,
						0 3px 0 #efefef,
						0 4px 0 #efefef,
						0 12px 5px rgba(0, 0, 0, 0.1);
					animation: rotate ease-in-out 1s infinite alternate;
				}}

				p {{
					font-size: 20px;
					text-shadow: 0 1px 0 #efefef;
					animation: 5s ease 0s normal forwards 1 fadeIn;
				}}
			</style>
			<div class="container">
				<h1>{text1}</h1>
				<p>{text2}</p>
			</div>
		</div>
	</foreignObject>
</svg>
""",
        "glitch": lambda text1, text2, height, width: f"""<svg fill="none" viewBox="0 0 {width} {height}" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
	<foreignObject width="100%" height="100%">
		<div xmlns="http://www.w3.org/1999/xhtml">
			<style>
                .container {{
                font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji';
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin: 0;
                width: 100%;
                height: {height}px;
                /* background: linear-gradient(-45deg, #fc5c7d, #6a82fb, #05dfd7); */
                background: #333;
                background-size: 600% 400%;
                border-radius: 10px;
                /* color: white; */
                text-align: center;
                }}


                h1 {{
                text-align: center;
                color: #fff;
                font-size: 5em;
                letter-spacing: 8px;
                font-family: "Lucida Console", Monaco, monospace;	
                font-weight: 400;
                /*Create overlap*/
                
                margin: 0;
                line-height: 0;
                /*Animation*/
                
                animation: glitch1 2.5s infinite;
                }}

                h1:nth-child(2) {{
                color: #67f3da;
                animation: glitch2 2.5s infinite;
                }}

                h1:nth-child(3) {{
                color: #f16f6f;
                animation: glitch3 2.5s infinite;
                }}
                /*Keyframes*/

                @keyframes glitch1 {{
                0% {{
                    transform: none;
                    opacity: 1;
                }}
                7% {{
                    transform: skew(-0.5deg, -0.9deg);
                    opacity: 0.75;
                }}
                10% {{
                    transform: none;
                    opacity: 1;
                }}
                27% {{
                    transform: none;
                    opacity: 1;
                }}
                30% {{
                    transform: skew(0.8deg, -0.1deg);
                    opacity: 0.75;
                }}
                35% {{
                    transform: none;
                    opacity: 1;
                }}
                52% {{
                    transform: none;
                    opacity: 1;
                }}
                55% {{
                    transform: skew(-1deg, 0.2deg);
                    opacity: 0.75;
                }}
                50% {{
                    transform: none;
                    opacity: 1;
                }}
                72% {{
                    transform: none;
                    opacity: 1;
                }}
                75% {{
                    transform: skew(0.4deg, 1deg);
                    opacity: 0.75;
                }}
                80% {{
                    transform: none;
                    opacity: 1;
                }}
                100% {{
                    transform: none;
                    opacity: 1;
                }}
                }}

                @keyframes glitch2 {{
                0% {{
                    transform: none;
                    opacity: 0.25;
                }}
                7% {{
                    transform: translate(-2px, -3px);
                    opacity: 0.5;
                }}
                10% {{
                    transform: none;
                    opacity: 0.25;
                }}
                27% {{
                    transform: none;
                    opacity: 0.25;
                }}
                30% {{
                    transform: translate(-5px, -2px);
                    opacity: 0.5;
                }}
                35% {{
                    transform: none;
                    opacity: 0.25;
                }}
                52% {{
                    transform: none;
                    opacity: 0.25;
                }}
                55% {{
                    transform: translate(-5px, -1px);
                    opacity: 0.5;
                }}
                50% {{
                    transform: none;
                    opacity: 0.25;
                }}
                72% {{
                    transform: none;
                    opacity: 0.25;
                }}
                75% {{
                    transform: translate(-2px, -6px);
                    opacity: 0.5;
                }}
                80% {{
                    transform: none;
                    opacity: 0.25;
                }}
                100% {{
                    transform: none;
                    opacity: 0.25;
                }}
                }}

                @keyframes glitch3 {{
                0% {{
                    transform: none;
                    opacity: 0.25;
                }}
                7% {{
                    transform: translate(2px, 3px);
                    opacity: 0.5;
                }}
                10% {{
                    transform: none;
                    opacity: 0.25;
                }}
                27% {{
                    transform: none;
                    opacity: 0.25;
                }}
                30% {{
                    transform: translate(5px, 2px);
                    opacity: 0.5;
                }}
                35% {{
                    transform: none;
                    opacity: 0.25;
                }}
                52% {{
                    transform: none;
                    opacity: 0.25;
                }}
                55% {{
                    transform: translate(5px, 1px);
                    opacity: 0.5;
                }}
                50% {{
                    transform: none;
                    opacity: 0.25;
                }}
                72% {{
                    transform: none;
                    opacity: 0.25;
                }}
                75% {{
                    transform: translate(2px, 6px);
                    opacity: 0.5;
                }}
                80% {{
                    transform: none;
                    opacity: 0.25;
                }}
                100% {{
                    transform: none;
                    opacity: 0.25;
                }}
                }}
			</style>
			<div class="container">
                <h1>{text1}</h1>
                <h1>{text1}</h1>
                <h1>{text1}</h1>
            </div>
        </div>
	</foreignObject>
</svg>""",
        "luminance": lambda text1,text2, height, width: f"""<svg fill="none" viewBox="0 0 {width} {height}" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
	<foreignObject width="100%" height="100%">
		<div xmlns="http://www.w3.org/1999/xhtml">
			<style>
                .container {{
                font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji';
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                margin: 0;
                width: 100%;
                height: ${height}px;
                background: #333641;
                background-size: 600% 400%;
                border-radius: 10px;
                color: white;
                text-align: center;
                }}
              
                .luminance {{
                background: 50% 100%/50% 50% no-repeat radial-gradient(ellipse at bottom, #fff, transparent, transparent);
                -webkit-background-clip: text;
                background-clip: text;
                color: transparent;
                font-size: 10vw;
                font-family:
						system-ui,
						-apple-system,
						'Segoe UI',
						Roboto,
						Helvetica,
						Arial,
						sans-serif,
						'Apple Color Emoji',
						'Segoe UI Emoji';
                -webkit-animation: reveal 3000ms ease-in-out forwards 200ms, glow 2500ms linear infinite 2000ms;
                        animation: reveal 3000ms ease-in-out forwards 200ms, glow 2500ms linear infinite 2000ms;
                }}
                @-webkit-keyframes reveal {{
                80% {{
                    letter-spacing: 8px;
                }}
                100% {{
                    background-size: 300% 300%;
                }}
                }}
                @keyframes reveal {{
                80% {{
                    letter-spacing: 8px;
                }}
                100% {{
                    background-size: 300% 300%;
                }}
                }}
                @-webkit-keyframes glow {{
                40% {{
                    text-shadow: 0 0 8px #fff;
                }}
                }}
                @keyframes glow {{
                40% {{
                    text-shadow: 0 0 8px #fff;
                }}
                }}
			</style>
			<div class="container">
                <div class="luminance">
                    {text1}
                </div>
            </div>
        </div>
	</foreignObject>
</svg> """,}

    error_svg = "origin"

    svg = svgs.get(type, svgs[error_svg])
    return svg(text1, text2, height, width), 200, {'Content-Type': 'image/svg+xml'}

if __name__ == '__main__':
    app.run(port=1234)
