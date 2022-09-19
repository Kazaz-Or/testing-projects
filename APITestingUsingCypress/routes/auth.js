const router = require('express').Router();
const User = require('../model/Users');
const { DataValidation } = require('../dataValidation');
const bcrypt = require('bcryptjs');
const Users = require('../model/Users');


router.post('/register', async (req, res) => {
    const {error} = DataValidation.registerValidation(req.body);
    if(error) return res.status(400).send(error.details[0].message);

    const emailExists = await User.findOne({ email: req.body.email });
    if (emailExists) return res.status(400).send('Email already exists');

    const encryptedPassword = await bcrypt.hash(req.body.password, 10);

    const user = new User({
        name: req.body.name,
        email: req.body.email,
        password: encryptedPassword
    });
    try {
        const savedUser = await user.save();
        res.send(savedUser);
    }catch (err) {
        res.status(400).send(err);
    }
});


router.post('/login', async (req, res) => {
    const {error} = DataValidation.loginValidation(req.body);
    if(error) return res.status(400).send(error.details[0].message);

    const userExists = await Users.findOne({email: req.body.email});
    if(!userExists) return res.status(400).send('Email not found');

    const validPassword = await bcrypt.compare(req.body.password, userExists.password);
    if(!validPassword) return res.status(401).send('Invalid password');

    res.status(200).send('Logged in successfully');
});


module.exports = router;
