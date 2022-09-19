const express = require('express');
const app = express();
const authRoute = require('./routes/auth');
const dotenv = require('dotenv');
const mongoose = require('mongoose');


dotenv.config();


mongoose.connect(process.env.DB_CONNECT, 
    { useNewUrlParser : true }, 
    () => console.log('Connected to DB'));


app.use(express.json());

app.use('/api/user', authRoute);
app.listen(3000, () => console.log('Server is running'));
