// import express from "express";
// import bodyParser from "body-parser";
var express = require("express");
var bodyParser = require("body-parser");
var app = express();
var User = require("./user").User;

app.use("public", express.static("public"));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({extended: true}));

app.set("view engine", "jade");

app.get("/", function(req, res){
    User.find(function(err, users){
        if (err) return console.error(err);
        res.render("index", {users: users});
    });
});

app.post("/", function(req,res){
    var user = new User({
        username: req.body.username,
        email: req.body.email,
        password: req.body.password
    });

    user.save().then(function(us){
        res.redirect("/");
    }, function(err){
        console.log(String(err));
        res.send("We can't save info");
    });
});

app.get("/delete", function(req, res){
    User.remove({username: req.query.username}).then(function(us){
        res.redirect("/"); 
    }, function(err){
        console.log(String(err));
        res.send("We can't remove user");
    });
});

app.listen(8080);