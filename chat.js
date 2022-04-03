class chat {
    constructor() {
        this.args = {
            output: document.querySelector('.main'),
            send: document.querySelector('.send')
        };

        this.messages = [];
    }

    display() {
        const {output, send} = this.args;

        send.addEventListener('click', () => this.onSendButton(output));

        const node = output.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") {
                this.onSendButton(output)
            }
        })
    }

    onSendButton(out) {
        var textField = out.querySelector('input');
        let text1 = textField.value;
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 };
        this.messages.push(msg1);

        fetch('http://127.0.0.1:5000/predict', {
            method: 'POST',
            body: JSON.stringify({ message: text1 }),
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(r => r.json())
            .then(r => {
                let msg2 = { name: "Sam", message: r.answer };
                this.messages.push(msg2);
                this.updateChatText(out);
                textField.value = ''
            }).catch((error) => {
            console.error('Error:', error);
            this.updateChatText(out);
            textField.value = ''
        });
    }

    updateChatText(out) {
        var html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Sam")
            {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>'
            }
            else
            {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>'
            }
        });
        const chatmessage = out.querySelector('.output');
        chatmessage.innerHTML = html;
    }
}

const out = new chat();
out.display();