class chat {
    constructor() {
        this.args = {
        output: document.querySelector('.main'), // Selects the main element which contains all elements.
        send: document.querySelector('.send'), // Element for the send button.
        clear: document.querySelector('.clear'), // Element for the clear button.
        history: document.querySelector('.history'), // Element for the history button.
        back: document.querySelector('.back') 
    };
    this.messages = [];
}
    main() {
        const {output, send, clear, history, back} = this.args;
        send.addEventListener('click', () => this.send(output)); // Adds a click event listener to the send button to run the send() method.  
        clear.addEventListener('click', () => this.clear()); // Adds a click event listener to the clear button to run the clear() method.
        history.addEventListener('click', () => this.history()); // Adds a click event listener to the history button that runs history(). 
        back.addEventListener('click', () => this.back()); // Adds a click event listener to the back button that runs back()
        const node = output.querySelector('input');  
        node.addEventListener("keyup", ({key}) => { // This allows for us to hit enter on the text box to run the send()
            if (key === "Enter") this.send(output)
        })
        this.sendSuggestion(output);
    }
    /**
     * Clears the text from the input.
     */
    clear() {
        document.getElementById ("msg").value = "";
    }

    /**
     * Navigates to the index html
     */
    help()
    {
        window.open("../html/index.html", "_self");
    }
    /**
     * Saves the chat log to a note file.
     */
     history() {
        let copy_messages = [];
        let html = "Niagara Games 2022 Chatbot Conversation History \n\n";

        for (let i=5 ; i<this.messages.length ; i++) {
            if ( this.messages[i].message != "Information about Canada Summer Games..." && this.messages[i].message != "Information about Niagara..." && this.messages[i].message != "Information about Sports..." && this.messages[i].message != "Information about Players..." ) {
                if ( (this.messages[i].name == "Bot" && this.messages[i].message != "Here are some clickable questions below:") || this.messages[i].name == "User" ) {
                    copy_messages.push(this.messages[i]);
                }
            }

            else if ( this.messages[i].message == "Information about Canada Summer Games..." || this.messages[i].message == "Information about Niagara..." || this.messages[i].message == "Information about Sports..." || this.messages[i].message == "Information about Players..." ) {
                if ( (i+1) < this.messages.length && this.messages[i+1].message != "Here are some clickable questions below:") {
                    copy_messages.push(this.messages[i]);
                }
            }
        }

        for (let i=0 ; i<copy_messages.length ; i++) {
            if ( i%2 === 0 ) {
                html += "User: ";
                let a = copy_messages[i].message.split("<br>");
                for ( let j=0 ; j<a.length ; j++ ) {
                    html += a[j] + "\n";
                }
            }
           
            else {
                html += "Bot: ";
                let a = copy_messages[i].message.split("<br>");
               
                for ( let j=0 ; j<a.length ; j++ ) {
                    let a1 = a[j].split("<br/>");
                    for (let h=0 ; h<a1.length ; h++ ) {
                        html += a1[h] + "\n";
                    }
                }
                html += "\n";
            }
        }
       
        var historyFile = new Blob([html], {type: "text/plain;charset=utf-8"});
        saveAs(historyFile, "NiagaraGames_Chatbot.txt");
    }
    
    /**
     * Back button leads to the index page.
     */
    back() {
        window.open("../html/index.html", "_self");
    }

    /**
    * This method takes the input in the textbox and sends it out to the predict method in the app backend.
    * Predict will process the input and return a response.
    * 
    * @param {Element} out: An element which should contain another element of the class input.
    */
    send(out) {
        
        let content = out.querySelector('input').value; // out is the document/page and we get the text from the input element.
        if (content === "") return;
        let msg1 = { name: "User", message: content }; 
        this.messages.push(msg1); // Takes the string from input and adds it to the messages array.
        this.update(out); // Takes the 

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: content }),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(r => r.json())
            .then(r => {
                let msg2 = { name: "Bot", message: r.answer };
                this.messages.push(msg2);
                setTimeout(() => {  this.update(out); }, 3000);
                this.clear();
            }).catch((error) => {
            console.error('Error:', error);
            setTimeout(() => {  this.update(out); }, 3000);
            this.clear();
        });

    }

    /**
     * This sends out suggestion questions to the user so they can pick them without having to guess what to ask the bot.
     * @param {Element} out: The element that is the main class.
     */
    sendSuggestion(out){
        let suggestion = "Welcome to the Chatbot, ask me questions and I'll try to answer them, here are some suggestion questions:"
        let suggestion1 = { name: "Bot", message: suggestion }; 
        let suggestion2 = { name: "Quick1", message: "Information about Canada Summer Games..."}; 
        let suggestion3 = { name: "Quick2", message: "Information about Niagara..."};
        let suggestion4 = { name: "Quick3", message: "Information about Sports..."};
        let suggestion5 = { name: "Quick4", message: "Information about Players..."};
        this.messages.push(suggestion1, suggestion2, suggestion3, suggestion4, suggestion5)
        this.update(out)
    }
    /**
     * This will take  a string and insert it into the text field so it can be sent out.
     * @param {Element} 
     */
    inputTextInTextBox(out, text){
        out.querySelector('input').value = text
    }

    /**
     * This will take text and input it in the textbox, then hits send.
     * @param {Element} out: This is the main element used.
     * @param {string} text: This is the string which needs to be sent.
     */
    inputAndSendText(out, text){
        this.inputTextInTextBox(out, text);
        this.send(out);
    }

    /**
    * This method takes an element and outputs a new message to the textbox.
    * @param {Element} out: An element which should contain another element of the class input.
    */
    update(out) {
        const options = { defaultProtocol: 'https', target: "_blank", format: (value, type) =>{
            if(type === 'url' && value.length > 38){
                value = "Get More Info Here"
            }
            return value;
        }};
        let html = ''; 
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Bot") { // Messages is a tuple of (name, message) if name is bot we add the proper elements.
                
                html += '<div class="messages visitor">' + linkifyHtml(item.message, options) + '</div>'
            } else if (item.name === "Quick"){ // Quick is the name of non-terminal suggestive options.
                
                html += '<div class="messages quick-reply">' + linkifyHtml(item.message, options) + '</div>'; 
            } else if (item.name =="Quick1" || item.name =="Quick2" || item.name =="Quick3" || item.name =="Quick4" || item.name =="Quick5"){ // Checks to see if the message is a quick-reply.
                
                html += '<div class="messages quick-suggest">' + linkifyHtml(item.message, options) + '</div>';
            }
            
            else { // Sets up the user messages.
                if (index === 0) {
                    html += '<div class="text-center"> <div class="spinner-border text-dark p-1" style="width: 2rem; height: 2rem;"> </div> </div>'
                    html += '<div class="messages bot">' + item.message + '</div>'
                }

                else { 
                    html += '<div class="messages bot">' + item.message + '</div>'
                }
            }
        });
        
        
        out.querySelector('.output').innerHTML = html;

        let replies = document.querySelectorAll('.quick-reply')
        replies.forEach((reply) => {
            reply.addEventListener('click', () =>{
                this.inputAndSendText(out, reply.textContent);
            });
        });

        let suggests = document.querySelectorAll('.quick-suggest')
        suggests.forEach((suggestion) => {
            suggestion.addEventListener('click', () =>{
                this.quickMessageSelect(out, suggestion.textContent);
            })
        })

        this.scrollFix(out.querySelector('.output'));
    }

    /**
     * Quick method to make a quick check on the text to see which category it belongs in.
     * @param {*} text: The name of the message which can either be Bot || quickX || User 
     * @returns true if we have a QuickX text. 
     */
    checkQuickMessage(text){
        if(text =="Quick1" || text =="Quick2" || text =="Quick3" || text =="Quick4" || text =="Quick5"){
            return true;
        } else{
            return false;
        }
    }

    /**
     * The switch statements which push out the clickable quick reply messages based on the suggestion clicked.
     * @param {Element} out: The main element.
     * @param {string} message: The suggestion message that was clicked.
     */
    quickMessageSelect(out, message){
        switch(message){
            case "Information about Canada Summer Games...":
                this.quickMessage1Push(out, "Information about Canada Summer Games...");
                break;
            case "Information about Niagara...":
                this.quickMessage2Push(out, "Information about Niagara...");
                break;
            case "Information about Sports...":
                this.quickMessage3Push(out,"Information about Sports..." )
                break;
            case "Information about Players...":
                this.quickMessage4Push(out, "Information about Players...")
                break;
        }

    }

    /**
     * The suggested message that was clicked on that introduced quick message 1
     * @param {Element} out: .main element containing all the elements.
     * @param {string} origMessage : The suggsested message clicked on to get here.
     */
    quickMessage1Push(out, origMessage){
        let message0 = { name: "User", message: origMessage}
        let message01 = { name: "Bot", message: "Here are some clickable questions below:"}
        let message1 = { name: "Quick", message: "What is the Canada Summer Games website?"}
        let message2 = { name: "Quick", message: "When does Canada Summer Games begin?"}
        let message3 = { name: "Quick", message: "Updates on the Canada Summer Games?"}
        let message4 = { name: "Quick", message: "Where is the Canada Summer Games?"}
        let message5 = { name: "Quick", message: "Where can I buy tickets?"}

        this.messages.push(message0, message01,message1, message2, message3, message4, message5)
        this.update(out)
    }
    
    /**
     * The suggested message that was clicked on that introduced quick message 2
     * @param {Element} out:  .main element containing all the elements.
     * @param {string} origMessage: The suggsested message clicked on to get here.
     */
    quickMessage2Push(out, origMessage){
        let message0 = { name: "User", message: origMessage}
        let message01 = { name: "Bot", message: "Here are some clickable questions below:"} 
        let message1 = { name: "Quick", message: "What transportation options are available?"}
        let message2 = { name: "Quick", message: "Is there an app for buses?"}
        let message3 = { name: "Quick", message: "What can you do in the Niagara region?"}
        let message4 = { name: "Quick", message: "Where can you stay in the Niagara region?"}
        let message5 = { name: "Quick", message: "What are the COVID-19 restrictions like in Niagara?"}

        this.messages.push(message0, message01,message1, message2, message3, message4, message5)
        this.update(out)
    }

    /**
     * The suggested message that was clicked on that introduced quick message 3
     * @param {Element} out: .main element containing all the elements.
     * @param {string} origMessage: The suggsested message clicked on to get here.
     */
    quickMessage3Push(out, origMessage){
        let message0 = { name: "User", message: origMessage}
        let message01 = { name: "Bot", message: "Here are some clickable questions below:"} 
        let message1 = { name: "Quick", message: "When is the next Baseball game?"}
        let message2 = { name: "Quick", message: "Ontario's next baseball game"}
        let message3 = { name: "Quick", message: "When is the next Basketball game?"}
        let message4 = { name: "Quick", message: "How many medals does Ontario have?"}

        this.messages.push(message0, message01,message1, message2, message3, message4)
        this.update(out)
    }

    /**
     * The suggested message that was clicked on that introduced quick message 4
     * @param {Element} out: .main element containing all the elements.
     * @param {*} origMessage: The suggsested message clicked on to get here.
     */
    quickMessage4Push(out, origMessage){
        let message0 = { name: "User", message: origMessage}
        let message01 = { name: "Bot", message: "Here are some clickable questions below:"} 
        let message1 = { name: "Quick", message: "Tell me about Evelyn Beaton"}
        let message2 = { name: "Quick", message: "What sport does Evelyn Beaton play?"}

        this.messages.push(message0, message01,message1, message2)
        this.update(out)
    }
        

    scrollFix(e) {
        e.scrollTop = e.scrollHeight;
    }
}
const out = new chat();
out.main();