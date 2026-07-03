tsParticles.load({
    id: "tsparticles",

    options: {

        fpsLimit:60,

        background:{
            color:"transparent"
        },

        particles:{

            number:{
                value:90
            },

            color:{
                value:"#00ff66"
            },

            shape:{
                type:"circle"
            },

            opacity:{
                value:0.6
            },

            size:{
                value:3
            },

            move:{
                enable:true,
                speed:2
            },

            links:{
                enable:true,
                color:"#00ff66",
                distance:150,
                opacity:0.3
            }

        }

    }

});