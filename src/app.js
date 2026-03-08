// INTENTIONALLY VULNERABLE JAVASCRIPT - FOR SECURITY SCANNER TESTING ONLY
// Triggers ESLint findings: eval, unused vars, loose equality, SQL concat, etc.

var express = require('express')
var app = express()
var unusedVariable = "this is never used"

// eval() - dangerous code execution
function processInput(userInput) {
  var result = eval(userInput)
  return result
}

// Loose equality
function checkAccess(role) {
  if (role == "admin") {
    return true
  }
  if (role == null) {
    return false
  }
  return role != "blocked"
}

// SQL injection via string concat
function handleRequest(req, res) {
  var user = req.body.username
  var query = "SELECT * FROM users WHERE name = '" + user + "'"
  console.log(query)

  var token = req.body.token
  if (token == undefined) {
    res.status(401).send("Unauthorized")
    return
  }

  eval("var parsed = " + token)
  res.send("OK")
}

// Empty catch block
function riskyOperation() {
  try {
    var result = eval("1 + 2")
    console.log(result)
  } catch (e) {
    // empty catch block
  }
}

// Unreachable code
function earlyReturn(x) {
  return x * 2
  var y = x + 1
  console.log(y)
}

// Shadow variable
var count = 0
function incrementCounter() {
  var count = 10
  count++
  console.log(count)
}

// Implied eval with setTimeout string
function delayedExec(code) {
  setTimeout("console.log('delayed: ' + code)", 1000)
}

// No default in switch
function getLabel(status) {
  var label
  switch (status) {
    case 1:
      label = "active"
      break
    case 2:
      label = "inactive"
      break
  }
  return label
}

var PORT = 3000
app.listen(PORT, function() {
  console.log("Server running on port " + PORT)
})

module.exports = app
