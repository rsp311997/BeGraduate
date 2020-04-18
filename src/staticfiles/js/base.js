// auth page js
function toggle(e){
    if(e.target.id === "login-btn"){
        let loginForm = document.getElementById("login-form");
        let signupForm = document.getElementById("signup-form");
        let signupButton = document.getElementById("signup-btn");
        let loginButton = document.getElementById("login-btn");
        loginForm.hidden=false;
        signupForm.hidden=true;
        signupButton.style="background-color:white;";
        loginButton.style="background-color:rgba(0,0,0,0.2);";
    }else{
        let loginForm = document.getElementById("login-form");
        let signupForm = document.getElementById("signup-form");
        let signupButton = document.getElementById("signup-btn");
        let loginButton = document.getElementById("login-btn");
        loginForm.hidden=true;
        signupForm.hidden=false;
        signupButton.style="background-color:rgba(0,0,0,0.2);";
        loginButton.style="background-color:white;";
    }
}
let login_tab = document.getElementById("login-tab");
let signup_tab = document.getElementById("signup-tab");

if(login_tab !== null){
    login_tab.addEventListener(
            "click",
            toggle
    );
}

if(signup_tab !== null){
    signup_tab.addEventListener(
            "click",
            toggle
    );
}

// home page js
function filter_toggle(e){
    let filter_btn_tab = document.getElementById("filter-btn-tab");
    let filter_tab = document.getElementById("filter-tab");

    filter_btn_tab.hidden=true;
    filter_tab.hidden=false;
}

let filter_btn = document.getElementById("filter-btn")

if(filter_btn){
    filter_btn.addEventListener(
        "click",
        filter_toggle
    );
}

// home page collapes
function collaps_tab_function(e){
    let collaps_tab=document.getElementsByClassName(e.target.attributes.value.value);
    let base_name=collaps_tab[0].className.split("-")[0];
    let end_name=collaps_tab[0].className.split("-")[1];

    let collaps_tab_basic=document.getElementsByClassName(base_name+"-basic");
    let collaps_tab_pics=document.getElementsByClassName(base_name+"-pics");
    let collaps_tab_heads=document.getElementsByClassName(base_name+"-heads");
    let collaps_tab_reviews=document.getElementsByClassName(base_name+"-reviews");
    let collaps_tab_description=document.getElementsByClassName(base_name+"-description");

    if(end_name==="basic"){
        if(collaps_tab_basic[0].hidden===true){
            collaps_tab_basic[0].hidden=false;
        }else{
            collaps_tab_basic[0].hidden=true;
        }
        collaps_tab_pics[0].hidden=true;
        collaps_tab_heads[0].hidden=true;
        collaps_tab_reviews[0].hidden=true;
        collaps_tab_description[0].hidden=true;
    }else if(end_name==="pics"){
        if(collaps_tab_pics[0].hidden===true){
            collaps_tab_pics[0].hidden=false;
        }else{
            collaps_tab_pics[0].hidden=true;
        }
        collaps_tab_basic[0].hidden=true;
        collaps_tab_heads[0].hidden=true;
        collaps_tab_reviews[0].hidden=true;
        collaps_tab_description[0].hidden=true;
    }else if(end_name==="heads"){
        if(collaps_tab_heads[0].hidden===true){
            collaps_tab_heads[0].hidden=false;
        }else{
            collaps_tab_heads[0].hidden=true;
        }
        collaps_tab_basic[0].hidden=true;
        collaps_tab_pics[0].hidden=true;
        collaps_tab_reviews[0].hidden=true;
        collaps_tab_description[0].hidden=true;
    }else if(end_name==="reviews"){
        if(collaps_tab_reviews[0].hidden===true){
            collaps_tab_reviews[0].hidden=false;
        }else{
            collaps_tab_reviews[0].hidden=true;
        }
        collaps_tab_basic[0].hidden=true;
        collaps_tab_heads[0].hidden=true;
        collaps_tab_pics[0].hidden=true;
        collaps_tab_description[0].hidden=true;
    }else if(end_name==="description"){
        if(collaps_tab_description[0].hidden===true){
            collaps_tab_description[0].hidden=false;
        }else{
            collaps_tab_description[0].hidden=true;
        }
        collaps_tab_basic[0].hidden=true;
        collaps_tab_heads[0].hidden=true;
        collaps_tab_reviews[0].hidden=true;
        collaps_tab_pics[0].hidden=true;
    }

}

let basic_collaps_btn = document.getElementsByClassName("basic_btn");
let heads_collaps_btn = document.getElementsByClassName("heads_btn");
let reviews_collaps_btn = document.getElementsByClassName("reviews_btn");
let discription_collaps_btn = document.getElementsByClassName("description_btn");
let pics_collaps_btn = document.getElementsByClassName("pics_btn");


if(basic_collaps_btn.length !== 0){
    for(let i=0;i<basic_collaps_btn.length;i++){
        basic_collaps_btn[i].addEventListener(
            "click",
            collaps_tab_function
        );
        heads_collaps_btn[i].addEventListener(
            "click",
            collaps_tab_function
        );
        reviews_collaps_btn[i].addEventListener(
            "click",
            collaps_tab_function
        );
        discription_collaps_btn[i].addEventListener(
            "click",
            collaps_tab_function
        );
        pics_collaps_btn[i].addEventListener(
            "click",
            collaps_tab_function
        );

    }
}

// review page collapes
function review_form_collaps(e){
    let review_form = document.getElementById("review-form");
    let review_form_btn = document.getElementById("review-form-btn");
    if(review_form.hidden == false){
        review_form.hidden = true;
        review_form_btn.firstChild.data="Add review";
    }else{
        review_form.hidden = false;
        review_form_btn.firstChild.data="Close";
    }
}

let review_form_btn = document.getElementById("review-form-btn");

if(review_form_btn){
    review_form_btn.addEventListener(
        "click",
        review_form_collaps
    );
}
