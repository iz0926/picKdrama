// defining lists for randomizer
// each list represents a trope and contains kdrama titles
var richboypoorgirl = [
    "Boys Over Flower", "Alchemy of Souls", "Crazy Love","The Heirs","A Business Proposal","The King: Eternal Monarch","Abyss","What\’s Wrong with Secretary Kim",
    "Coffee Prince","Goblin","My Secret Romance","Strong Woman Do Bong Soon","The Legend of the Blue Sea","Cinderella and Four Knights","Love in the Moonlight"
]

var richgirlpoorboy = [
    "K2", "High Society", "Mr. Sunshine", "That Winter, The Wind Blows", "That Fool", "It\’s Okay to Not be Okay", "Secret Love Affair","Yong Pal","Hotel King",
    "The Snow Queen","Innocent Man","My Fair Lady","Temptation","Crash Landing on You","Encounter","The Beauty Inside","Hotel Del Luna"
]

var friendstolovers = [
    "Reply 1997","Weightlifting Fair Kim Bok Joo","Fight for My Way","Our Beloved Summer","Dr. Romantic 2","Hospital Playlist","Reply 1988","School 2017",
    "Romance is a Bonus Book","More Than Friends","One Spring Night","Something in the Rain","I Need Romance 2","Romance is a Bonus Book","Love is for Suckers","Shooting Stars"
]

var lovetriangle = [
    "Scarlet Heart: Ryeo","She Was Pretty","Who Are You: School 2015","Hwarang","Fated to Love You","Cheese in the Trap","I\’ll Go to You When the Weather is Nice",
    "Nevertheless","Love Alarm","The Liar and his Lover","While You Were Sleeping","Record of Youth","Extraordinary You","A Love so Beautiful","Hometown Cha-Cha-Cha"
]

var contractrelationship = [
    "Marriage Contract","Marriage not Dating","Because this is my first love","Full House","The Beauty Inside","Because this is my first life","Love in Contract",
    "Business Proposal","Crash Landing on You","Her Private Life","So I Married an Anti-fan","Happiness","Something about 1%","My Roommate is a Gumiho"
]

    // function that is called when one of the 5 trope buttons is clicked
    // one of the lists is passed in as argument to get a random number based on the number of titles in list
    //"newRecSection"
    function getRecs(array) {
        const randomElement = array[Math.floor(Math.random() * array.length)]
        document.getElementById("newRecSection").innerHTML=randomElement;
    }

    // source: (https://css-tricks.com/play-button-youtube-and-vimeo-api/)
    // callback function that the Youtube API will use
    // Connects the videos to their buttons
    function onYouTubePlayerAPIReady() {
        player = new YT.Player('video', {
            events: {
                'onReady': onPlayerReady
            }
        });
        player2 = new YT.Player('vid2', {
            events: {
                'onReady': onPlayerReady
            }
        })
        player3 = new YT.Player('vid3', {
            events: {
                'onReady': onPlayerReady
            }
        })
        player4 = new YT.Player('vid4', {
            events: {
                'onReady': onPlayerReady
            }
        })
    }
    function onPlayerReady(event) {
        // bind events
        // Makes the commands play/pause possible
        var playButton = document.getElementById("video1");
        playButton.addEventListener("click", function() {
            player.playVideo();
        });

        var pauseButton = document.getElementById("video2");
            pauseButton.addEventListener("click", function() {
                player.pauseVideo();
        });
        let video3 = document.getElementById("video3");
            video3.addEventListener('click', () => {
                player2.playVideo();
            })

        let video4 = document.getElementById("video4");
            video4.addEventListener('click', () => {
                player2.pauseVideo();
            })
        let video5 = document.getElementById("video5");
            video5.addEventListener('click', () => {
                player3.playVideo();
            })

        let video6 = document.getElementById("video6");
            video6.addEventListener('click', () => {
                player3.pauseVideo();
            })
        let video7 = document.getElementById("video7");
            video7.addEventListener('click', () => {
                player4.playVideo();
            })

        let video8 = document.getElementById("video8");
            video8.addEventListener('click', () => {
                player4.pauseVideo();
            })
    }

    // Youtube API script
    var tag = document.createElement('script');
    tag.src = "//www.youtube.com/player_api";
    var firstScriptTag = document.getElementsByTagName('script')[0];
    firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

    // variables relating to each video
    var player;
    var player2;
    var player3;
    var player4;


