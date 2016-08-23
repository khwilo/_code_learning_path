var secret = 'zoltan';

module.exports = {
    name: 'Packt',

    lower: function (input) {
        return input.toLowerCase();
    },

    upper: function (input) {
        return input.toUpperCase();
    },

    get_name: function (input) {
        return this.name;
    },

    get_secret: function (input) {
        return secret;
    }
};