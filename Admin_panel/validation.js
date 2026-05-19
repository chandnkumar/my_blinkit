$('.lostfocus').on('focusout', function () {
    v = $(this).val();
    if (v.length == 0) {
        $(this).val("*Field is mandatory");
        // $(this).css("border","2px solid red");
        // $(this).css("color","red");
        $(this).css({ "border": "2px solid red", "color": "red" });
    }
});

$('.gainfocus').on('focus', function () {
    v = $(this).val();
    if (v == "*Field is mandatory") {
        $(this).val("");
        // $(this).css("border","2px solid red");
        // $(this).css("color","red");
        $(this).css({ "border": "2px solid black", "color": "black" });

    }
})


// only digit are allowed 
// $('.onlydigits').on('keypress', function (e) {
//     ch = e.which
//     $(this).siblings('span').text("");
//     v = $(this).val();
//     $(this).siblings('span').css('color', 'red');
//     if (this.selectionStart === 0 && (ch == 48 || ch == 32)) {
//         $(this).siblings('span').text("At first position zero or space are not allowed");
//         return false;
//     }
//     else if (!(ch >= 48 && ch <= 57)) {
//         $(this).siblings('span').text("Only digits are allowed");
//         return false;
//     }
//     else if (v.length == 10) {
//         $(this).siblings('span').text("Only 10 digits are allowed");
//         return false;
//     }
//     else if(v.slice(-1)==' ' && ch==32)
//     {
//         $(this).siblings('span').text("Consecutive spaces not allowed");
//         return false; 
//     }
// })

$('.onlydigits').on('keydown', function (e) {
    let ch = e.key;
    let v = $(this).val();
    let span = $(this).siblings('span');
    span.text("").css('color', 'red');

    // Block first character as 0 or space
    if (this.selectionStart === 0 && (ch === "0" || ch === " ")) {
        span.text("At first position zero or space are not allowed");
        e.preventDefault();
    }
    // Allow only digits
    else if (!/^[0-9]$/.test(ch)) {
        if (!["Backspace", "Tab", "ArrowLeft", "ArrowRight", "Delete"].includes(ch)) {
            span.text("Only digits are allowed");
            e.preventDefault();
        }
    }
    // Limit to 10 digits
    else if (v.length >= 10) {
        span.text("Only 10 digits are allowed");
        e.preventDefault();
    }
});


// alert("this is working")

// summit error

// $('.create').on('click', function () {
//     p = ['#user_id','#full_name','#user_no','#emp_email','#emp_idproof']
//     for (a in p) {
//         a = p[a]
//         if ($(a).val().length === 0 ||$(a).val()==="*Field is mandatory") {
//             $(a).css({ "border": "2px solid red","color": "red" });
//             $(a).val("*Field is mandatory");
//         }
//     }
// })



// reset btn
$('.reset').on('click', function () {
    p = ['.lostfocus']
    for (a in p) {
        a = p[a]
        if ($(a).val().length == 0 ||$(a).val()=="*Field is mandatory") {
            $(a).css({ "border": "2px solid black","color": "black" });
            $(a).val("");
        }
    }
}) 

$('.reset').click(function () {
    $('form')[0].reset();

});

// Consecutive spaces not allowed

$(".Consecutive").on('keypress', function(e){
    ch=e.which
    $(this).siblings('span').text("");
    v=$(this).val();
    $(this).siblings('span').css('color','red');
    if(this.selectionStart===0 && ch==32)
    {
        $(this).siblings('span').text("At first position space not allowed");
        return false;
    }    
    else if(v.slice(-1)==' ' && ch==32)
    {
        $(this).siblings('span').text("Consecutive spaces not allowed");
        return false;
    }
    // else if(!((ch>=65 && ch<=90) || (ch>=97 && ch<=122) || ch==32))
    // {
    //     $(this).siblings('span').text("Only alphabets and space allowed");
    //     return false;
    // }    
})
