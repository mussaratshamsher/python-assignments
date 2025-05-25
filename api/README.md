<.....To Deploy on vercel.....>

Add config in vercel.json

{ "version": 2, "builds": [ { "src": "main.py", "use": "@vercel/python", "config": { "runtime": "python3.9" } } ], "routes": [ { "src": "/(.*)", "dest": "/main.py" } ] }

<....Add in requirement.txt.....> fastapi[standard] fastapi==0.75.0 uvicorn==0.17.0

Push folder into your github

Deploy on vercel , same as other projects

Don't worry to see not found after deploy, just open link, 
add endpoint defined in your project NEXT to vercel url.
In my project /products & you will get all products

To search a single product use /products/1 or etc
