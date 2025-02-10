(function (window, undefined) {
    window.Asc.plugin.init = function () {
        // this.callCommand(function() {
        //     var oDocument = Api.GetDocument();
        //     var oParagraph = Api.CreateParagraph();
        //     oParagraph.AddText("Hello world!");
        //     oDocument.InsertContent([oParagraph]);
        // }, true);
    };
    window.Asc.plugin.button = function (id) {
        console.log(id)
        this.executeCommand("close", '');
    };


//     var blob = new Blob([arrayBufferWithPNG], {type: "image/png"}),
//     url = URL.createObjectURL(blob),
//     img = new Image();

// img.onload = function() {
//     URL.revokeObjectURL(this.src);     // clean-up memory
//     document.body.appendChild(this);   // add image to DOM
// }

// img.src = url;                         // can now "stream" the bytes

//-------------------------------------------
// var formData = new FormData();
// formData.append('file', $('#fileInput')[0].files[0]);

// $.ajax({
//     type: 'POST',
//     url: 'upload.php',
//     data: formData,
//     processData: false,
//     contentType: false,
//     success: function(response) { console.log('Успешная загрузка:', response); },
//     error: function(jqXHR) { console.log('Возникла ошибка при загрузке:', jqXHR.responseText); }
// });
})(window, undefined);