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

<img width="897" height="659" alt="Screenshot 2026-02-03 175332" src="https://github.com/user-attachments/assets/07110f97-923b-4110-9d83-7c238a915a76" />

Botpress Studio Setup to create new chatbot:
1. Click-> https://botpress.com/features/ai-agent-studio     
2. Get Started for free
3. Select Botpress Studio
4. Name your bot(Click next)->You can also skip this->But I do give name to it
5. Select other from the 4 options ->you can also skip this
6. Describe what kind of bot you want-> it's also skippable
7. Give link of your website->I skipped this step(If you give link of the site botpress train the bot according to your website & also add the functionalities of it)
8. After skipping, you will get into the Workflow here
9. Autonomous Node->Where AI is integrated->In this, we tell our bot what its purpose is
10. In Knowledge Base->Here we can give urls, apis, pdf & html links->In this I have uploaded a documentation(Which include whole buttons symptoms everything)
11. Then, in workflow, I have given a card & selected search knowledge
12. If we want to call a user name, then we can assign a variable for it, but I have not done that
13. After setting information Click on the emulator & test your bot, is it working according to your specified commands.





    
