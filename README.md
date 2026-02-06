First Create virtual Environment:
1. Open the folder where the project exists, then in the search bar type cmd
2. Then type commands when the command prompt opens:
a)Create Virtual Environment= python -m venv venv
b) Activate virtual Environment= venv\Scripts\activate
3. Type these commands to install dependencies:
pip install flask
pip install pdfplumber
pip install beautifulsoup4
4. After the above implementations, type the following command:
     Flask run
5. Copy the localhost url
6 . Wait so that url bot runs successfully

The chatbot script that we can integrate into code is(it is integrated in my code):

<script src="https://cdn.botpress.cloud/webchat/v3.5/inject.js"></script>
<script src="https://files.bpcontent.cloud/2026/02/01/19/20260201192035-9CFMRLJ0.js" defer></script>

<img width="897" height="663" alt="image" src="https://github.com/user-attachments/assets/c8bce0d0-d5f8-4a9f-ba2b-4ff02b8c0d5b" />

Botpress Studio Setup to create a new chatbot:

1. Click-> https://botpress.com/features/ai-agent-studio
       <img width="1833" height="946" alt="Screenshot 2026-01-26 212451" src="https://github.com/user-attachments/assets/cd0aa190-2ac7-4dd0-b5db-287bb85e9ade" />
2. Get Started for free
3. Select Botpress Studio
4. Name your bot(Click next)->You can also skip this->But I do give name to it
5. Select other from the 4 options ->you can also skip this
6. Describe what kind of bot you want-> it's also skippable
7. Give the link of your website->I skipped this step(If you give the link of the site, botpresswill  train the bot according to your website & also add the functionalities of it)
8. After skipping, you will get into the Workflow here
    <img width="1919" height="889" alt="Screenshot 2026-01-26 213047" src="https://github.com/user-attachments/assets/6e69f71a-3f75-4cf4-a3e3-c6a6d1043dc9" />
9. Autonomous Node->Where AI is integrated->In this, we tell our bot what its purpose is
10. In Knowledge Base->Here we can give urls, apis, pdf & html links->In this I have uploaded a documentation(Which include whole buttons symptoms everything)
    <img width="1898" height="899" alt="Screenshot 2026-01-26 213617" src="https://github.com/user-attachments/assets/19574611-ea7e-467a-abdf-5538c98cbe03" />
11. Then, in workflow, I have given a card & selected search knowledge
    <img width="875" height="434" alt="Screenshot 2026-01-29 195656" src="https://github.com/user-attachments/assets/7aeaa877-dc47-46f8-bd7b-c2370d08e5c5" />
12. If we want to call a user name, then we can assign a variable for it, but I have not done that
13. After setting information Click on the emulator & test your bot, is it working according to your specified commands.
14. Below is my chatbot Botpress workflow:
    <img width="929" height="620" alt="Screenshot 2026-02-02 152538" src="https://github.com/user-attachments/assets/fc065065-13fb-47e9-8193-77d889fda27d" />

    
