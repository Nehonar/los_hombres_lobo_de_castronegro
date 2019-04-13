// import mongoose from "mongoose";
var mongoose = require("mongoose");
var schema = mongoose.Schema;

mongoose.connect("mongodb://localhost/users");

var email_match = [/^(([^<>()\[\]\.,;:\s@\"]+(\.[^<>()\[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i,"Email is not valid"]

var user_schema = new schema({
    username: {
        type: String, 
        required: true, 
        maxlength: [50, "Username too long"]
    },
    email: {
        type: String, 
        required: "Email is required",
        match: email_match
    },
    password: {
        type: String,
        minlength: [6, "Minimum six characters"]
    }
});

var User = mongoose.model("User", user_schema);
module.exports.User = User;