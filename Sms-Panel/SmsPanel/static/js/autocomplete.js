$(function () {
    // var d = JSON.parse(data)
    // // console.log('data : ', d)
    // const availableTags = []
    // for (var i = 0; i < d.length; i++) {
    //     availableTags.push(d[i].fields.name)
    // }
    // // var availableTags = ["ActionScript","AppleScript","Artificial Intelligence","Asp","Api","BASIC","C","C++","Clojure","COBOL","ColdFusion","Django","Erlang","Fortran",
    //     // "Groovy","Haskell","Java","JavaScript","jQuery","Lisp","Machine Learning","Node js","Perl","PHP","Python","Ruby","Ruby on Rails","Scala", "Scheme" ];
    // $("#search-book").autocomplete({
    //     source: function( request, response ) {
    //         var matcher = new RegExp( "^" + $.ui.autocomplete.escapeRegex( request.term ), "i" );
    //         response( $.grep( availableTags, function( item ){
    //             return matcher.test( item );
    //         }) );
    //     },
    //     // source: "/",
    //     // minLength: 2,
    //     select: function (event, ui) {
    //         AutoCompleteSelectHandler(event, ui)
    //     },
    // });
    // $('#print').on('click', function(){
    //     $("#home-content").css("display",'none')
    //     window.print('#mytable')
    //     $("#home-content").css("display", 'block')
    // })
    console.log('autocomplete ....')
    // var availableDepts = dept ;
    // var availableDesgs = desg ;
    // console.log('availableDept: ', availableDepts);
    // console.log('availableDesg: ', availableDesgs);
    var availableDepts = ["Affiliate","SMS","Information Technology","Native","Email","Logistic"] ;
    var availableDesgs = ["Junior Developer", "Senior Developer", "Manager", "UX Developer", "UI Developer"] ;
     // For DepartmentsavailableDesgs
    $("#id_department").autocomplete({
      source: availableDepts,
      select: function(event, ui){
        AutoCompleteSelectHandler(event, ui)
      }
    });
    //  For Departments
    $("#id_designation").autocomplete({
      source: availableDesgs,
      select: function(event, ui){
        AutoCompleteSelectHandler(event, ui)
      }
    });
});

function AutoCompleteSelectHandler(event, ui) {
    var selectedObj = ui.item;
    $('.ui-helper-hidden-accessible').css("display", "None")
    // console.log(selectedObj, ui)           // {label: "Email", value: "Email"}, { item :{label: "Email", value: "Email"} }
}
