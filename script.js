function showRegister() {
    document.getElementById('content').innerHTML = `
        <h2>Register</h2>
        <form onsubmit="register(event)">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required>
            <label for="password">Password</label>
            <input type="password" id="password" name="password" required>
            <button type="submit">Register</button>
        </form>
    `;
}

function showLogin() {
    document.getElementById('content').innerHTML = `
        <h2>Login</h2>
        <form onsubmit="login(event)">
            <label for="username">Username</label>
            <input type="text" id="username" name="username" required>
            <label for="password">Password</label>
            <input type="password" id="password" name="password" required>
            <button type="submit">Login</button>
        </form>
    `;
}

function showVote() {
    document.getElementById('content').innerHTML = `
        <h2>Vote</h2>
        <form onsubmit="vote(event)">
            <label for="candidate">Choose a candidate:</label>
            <select id="candidate" name="candidate" required>
                <option value="Candidate 1">Candidate 1</option>
                <option value="Candidate 2">Candidate 2</option>
                <option value="Candidate 3">Candidate 3</option>
            </select>
            <button type="submit">Vote</button>
        </form>
    `;
}

function showResults() {
    document.getElementById('content').innerHTML = `
        <h2>Results</h2>
        <div id="results">
            <ul>
                <li>Candidate 1: 10 votes</li>
                <li>Candidate 2: 5 votes</li>
                <li>Candidate 3: 3 votes</li>
            </ul>
        </div>
    `;
}

// The following functions are placeholders and should be replaced with actual logic
function register(event) {
    event.preventDefault();
    alert('User registered successfully');
}

function login(event) {
    event.preventDefault();
    alert('User logged in successfully');
}

function vote(event) {
    event.preventDefault();
    alert('Vote cast successfully');
}