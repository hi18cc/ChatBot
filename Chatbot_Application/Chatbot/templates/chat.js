class chat {
    args = {
        output: document.querySelector('.main'),
        send: document.querySelector('.send'),
        clear: document.querySelector('.clear')
    };

    messages = [];

    main() {
        const {output, send, clear} = this.args;

        send.addEventListener('click', () => this.send(output));

        clear.addEventListener('click', () => this.clear());

        const node = output.querySelector('input');
        node.addEventListener("keyup", ({key}) => {
            if (key === "Enter") this.send(output)
        })
    }

    clear() {
        document.getElementById ("msg").value = "";
    }

    send(out) {
        let content = out.querySelector('input').value;
        if (content === "") return;

        let msg1 = { name: "User", message: content };
        this.messages.push(msg1);

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
                this.update(out);
                this.clear();
            }).catch((error) => {
            console.error('Error:', error);
            this.update(out);
            this.clear();
        });
    }

    update(out) {
        let html = '';
        this.messages.slice().reverse().forEach(function(item, index) {
            if (item.name === "Bot") html += '<div class="messages visitor">' + item.message + '</div>'
            else html += '<div class="messages bot">' + item.message + '</div>'
        });
        out.querySelector('.output').innerHTML = html;
    }
}

const out = new chat();
out.main();