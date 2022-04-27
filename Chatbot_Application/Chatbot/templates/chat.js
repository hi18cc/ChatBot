class chat {
    constructor() {
        this.args = {
        output: document.querySelector('.main'),
        send: document.querySelector('.send'),
        clear: document.querySelector('.clear'),
        history: document.querySelector('.history'),
        back: document.querySelector('.back')
    };
    this.messages = [];
}
    main() {
        const {output, send, clear, history, back} = this.args;
        send.addEventListener('click', () => this.send(output));
        clear.addEventListener('click', () => this.clear());
        history.addEventListener('click', () => this.history());
        back.addEventListener('click', () => this.back());
        const node = output.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") this.send(output)
        })
        this.sendSuggestion(output);
    }
    clear() {
        document.getElementById ("msg").value = "";
    }

    help()
    {
        window.open("index.html", "_self");
    }
    
    history() {
        let html = "Niagara Games 2022 Chatbot Conversation History \n\n";

        for (let i=0 ; i<this.messages.length ; i++) {
            if ( i%2 === 0 ) {
                html += "User: ";
                let a = this.messages[i].message.split("<br>");

                for ( let j=0 ; j<a.length ; j++ ) {
                    html += a[j] + "\n";
                }
            }
            
            else {
                html += "Bot: ";
                let a = this.messages[i].message.split("<br>");
                
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
    
    back() {
        window.open("index.html", "_self");
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
        let suggestion = "Welcome to the Chatbot, ask me questions and I'll try to answer them, here are some suggestion questions;"
        let suggestion1 = { name: "Bot", message: suggestion }; 
        let suggestion2 = { name: "Quick", message: "How many medals does Ontario have?"}; 
        let suggestion3 = { name: "Quick", message: "What sport does Spencer Allen play?"};
        let suggestion4 = { name: "Quick", message: "Where can I buy tickets?"};
        this.messages.push(suggestion1, suggestion2, suggestion3, suggestion4)
        this.update(out)
    }
    /**
     * This will take  a string and insert it into the text field so it can be sent out.
     * @param {Element} 
     */
    inputTextInTextBox(out, text){
        out.querySelector('input').value = text
    }

    inputAndSendText(out, text){
        this.inputTextInTextBox(out, text);
        this.send(out);
    }

    /**
    * This method takes an element and outputs a new message to the textbox.
    * @param {Element} out: An element which should contain another element of the class input.
    */
    update(out) {
        
        let html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Bot") {
                const options = { defaultProtocol: 'https', target: "_blank" };
                html += '<div class="messages visitor">' + linkifyHtml(item.message, options) + '</div>'
            } else if (item.name === "Quick"){
                const options = { defaultProtocol: 'https', target: "_blank" };
                html += '<div class="messages quick-reply">' + linkifyHtml(item.message, options) + '</div>';
            }
            
            else {
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

        this.scrollFix(out.querySelector('.output'));
    }

    scrollFix(e) {
        e.scrollTop = e.scrollHeight;
    }
}
const out = new chat();
out.main();