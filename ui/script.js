document.getElementById('createRuleForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const ruleName = document.getElementById('ruleName').value;
    const ruleString = document.getElementById('ruleString').value;

    try {
        const response = await fetch('/create_rule', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ rule_name: ruleName, rule_string: ruleString })
        });
        const data = await response.json();
        document.getElementById('createRuleResponse').textContent = data.message || data.error;
    } catch (error) {
        document.getElementById('createRuleResponse').textContent = 'Error: ' + error.message;
    }
});

// document.getElementById('getRulesButton').addEventListener('click', async function() {
//     try {
//         const response = await fetch('/get_rules');
//         const data = await response.json();
//         const rulesList = document.getElementById('rulesList');
//         rulesList.innerHTML = '<ul>' + data.map(rule => `<li>${rule.name}: ${rule.rule_string}</li>`).join('') + '</ul>';
//     } catch (error) {
//         document.getElementById('rulesList').textContent = 'Error: ' + error.message;
//     }
// });


document.getElementById("getRulesButton").addEventListener("click", function () {
    fetch("/get_rules")
        .then(response => response.json())
        .then(data => {
            // Check if data is an array
            if (Array.isArray(data)) {
                const rulesList = document.getElementById("rulesList");
                rulesList.innerHTML = ""; // Clear existing rules
                data.map(rule => {
                    const ruleElement = document.createElement("li");
                    ruleElement.textContent = `${rule.name}: ${rule.rule_string}`;
                    rulesList.appendChild(ruleElement);
                });
            } else {
                console.error("Data is not an array:", data);
            }
        })
        .catch(error => console.error("Error fetching rules:", error));
});



document.getElementById('evaluateForm').addEventListener('submit', async function(event) {
    event.preventDefault();
    const ruleStrings = document.getElementById('ruleStrings').value.split(',');
    const attributes = JSON.parse(document.getElementById('attributes').value);

    try {
        const response = await fetch('/evaluate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ rule_strings: ruleStrings, attributes: attributes })
        });
        const data = await response.json();
        document.getElementById('evaluateResponse').textContent = 'Evaluation Result: ' + data.result;
    } catch (error) {
        document.getElementById('evaluateResponse').textContent = 'Error: ' + error.message;
    }
});
