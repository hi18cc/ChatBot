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
    }
    clear() {
        document.getElementById ("msg").value = "";
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
    send(out) {
        let content = out.querySelector('input').value;
        if (content === "") return;
        let msg1 = { name: "User", message: content };
        this.messages.push(msg1);
        this.update(out);

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
    update(out) {
        let html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Bot") {
				const options = { defaultProtocol: 'https' };
                html += '<div class="messages visitor">' + linkifyHtml(item.message, options) + '</div>'
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
        this.scrollFix(out.querySelector('.output'));
    }

    scrollFix(e) {
        e.scrollTop = e.scrollHeight;
    }
}
const out = new chat();
out.main();