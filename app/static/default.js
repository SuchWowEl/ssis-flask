
  //$(document).ready();
  tableUrl = "";// e.g. "/students/"
  search_filter = "";
  let selectedStudent = [];
  recently_added = "";


  // Function to toggle the visibility of dropdown-blocks
  function toggleDropdown() {
    var dropdownBlocks = document.getElementById("dropdown-blocks");
    if (dropdownBlocks.classList.contains("hidden")) {
      dropdownBlocks.classList.remove("hidden");
      dropdownBlocks.classList.add("block");
    } else {
      dropdownBlocks.classList.remove("block");
      dropdownBlocks.classList.add("hidden");
    }
  }

  // Function to handle clicks on the document
  function documentClickHandler(event) {
    var dropdownBlocks = document.getElementById("dropdown-blocks");
    
    if (
      $("#dropdown-blocks").length > 0 &&
      event.target.id !== "dropdown-blocks" &&
      event.target.id !== "dropdown-button"
    ) {
      dropdownBlocks.classList.remove("block");
      dropdownBlocks.classList.add("hidden");
    }
    if ($("#formDropdownBox").length > 0){
      var formDropdownBox = document.getElementById("formDropdownBox");
      
      if (
        event.target.id !== "formDropdownBox" &&
        event.target.id !== "formDropdownButton"
      ) {
        formDropdownBox.classList.remove("block");
        formDropdownBox.classList.add("hidden");
      }
    }
  }

  function filterDropdownChecker(){
    var thebox = document.getElementById("popupDropdownBox");
    if (thebox.classList.contains("show")){
      document.getElementById("popupDropdownBox").classList.remove("show");
      document.getElementById("popupDropdownBox").classList.add("hidden");
    }
    else{
      document.getElementById("popupDropdownBox").classList.add("show");
      document.getElementById("popupDropdownBox").classList.remove("hidden");
    }
  }
  
  // Function to handle clicks on dropdown-blocks
  function dropdownBlocksClickHandler(event) {
    if (event.target.tagName === "BUTTON") {
      var dropdownButton = document.getElementById("dropdown-button");
      var textNode = Array.from(dropdownButton.childNodes).find(function (
        node
      ) {
        return node.nodeType === 3; // Filter text nodes
      });
      textNode.replaceWith(event.target.textContent);
      search_filter = event.target.textContent.trim();
      if(["gender", "course", "college"].includes(search_filter)){
        document.getElementById("search-dropdown").classList.add("cursor-not-allowed");
        document.getElementById("search-dropdown").setAttribute("disabled", "true");
        document.getElementById("search_op_button").classList.add("cursor-not-allowed");
      }
      else{
        document.getElementById("search-dropdown").classList.remove("cursor-not-allowed");
        document.getElementById("search-dropdown").setAttribute("disabled", null);
        document.getElementById("search_op_button").classList.remove("cursor-not-allowed");
      }
    }
    console.log("search_filter");
    console.log(search_filter);
        
    if (["gender", "course", "college"].includes(search_filter)){
      console.log("search_filter gets in");
      if (search_filter == "gender"){
        localurl = "students/gender/retriever"
      }
      else if (search_filter == "course"){
        localurl = "courses/retriever"
      }
      else {
        localurl = "colleges/retriever"
      }

      $("#dropdown-to-replace").load(localurl, function(response) {
        var textNode = Array.from(document.getElementById("popupDropdownButton").childNodes).find(function (
          node
        ) {
          return node.nodeType === 3; // Filter text nodes
        });
        var genderChoice = textNode.textContent.trim(); 
        document.getElementById("filter-popup").classList.add("show");
        document.getElementById("filter-popup").classList.remove("hidden");

        document.getElementById("proceed-to-filter").addEventListener("click", 
        function(){
          const csrfToken = document
            .querySelector("meta[name=csrf-token]")
            .getAttribute("content");
          const formData = {
            header: search_filter,
            search: genderChoice
          };
          var queryString = $.param(formData);
          $.ajax({
            url: tableUrl + "search/?" + queryString,
            type: "GET",
            success: function(response){
              if (response["response"]===true){
                console.log("search success");
                const element = document.getElementById(tableUrl.slice(1, -1));

                // Check if the element exists (not null)
                if (element) {
                  // Programmatically trigger a click event
                  element.click();
                }
              }
              else {
                console.log("Failed");
                alert(response["response"]);
              }
            }
          });
          event.preventDefault();
        });
        document.getElementById("popupDropdownButton").addEventListener("click",filterDropdownChecker);
        document.getElementById("popupDropdownBox-choices").addEventListener("click", function(event) {
          console.log("dropdown chose");
          if (event.target.tagName === "BUTTON") {
            console.log("valid");
            var dropdownButton = document.getElementById("popupDropdownButton");
            var textNode = Array.from(dropdownButton.childNodes).find(function (
              node
            ) {
              return node.nodeType === 3; // Filter text nodes
            });
            textNode.replaceWith(event.target.textContent);
            genderChoice = event.target.textContent.trim();
            filterDropdownChecker();
          }
        });
      });
    }
    else{
      document.getElementById("search-dropdown").disabled = document.getElementById("search_op_button").disabled = false;
      document.getElementById("search-dropdown").classList.remove("cursor-not-allowed");
      document.getElementById("search_op_button").classList.remove("cursor-not-allowed");
    }
  }

  // Function to handle the click event on .btn-tabs elements
  function handleTabClick(event) {
    console.log("asdad");
    ["students", "courses", "colleges"].forEach(function (element) {
      document.getElementById(element).classList.remove("border-lime-400");
      document.getElementById(element).classList.add("border-transparent");
    });
    document.getElementById(event.target.id).classList.add("border-lime-400");
    document
      .getElementById(event.target.id)
      .classList.remove("border-transparent");

    console.log(tableUrl);
    tableUrl = "/" + event.target.id + "/";
    var content = document.getElementById("content");
    search_filter = "";
    
    fetch(tableUrl)
        .then((response) => {
          if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.status}`);
          }
          return response.text();
        })
        .then((data) => {
          const parser = new DOMParser();
          const doc = parser.parseFromString(data, "text/html");
          if (doc.querySelector("parsererror")) {
            console.error("HTML validation error");
          } else {
            content.innerHTML = data;
            tablePick();
          }
        })
        .catch((error) => {
          console.error("Fetch error:", error);
        });
      }

  function searchTable(event){
    console.log("SEARCHTABLE");
    searchUrl = tableUrl + "search/";
    const formData = {
      header: search_filter,
      search: document.getElementById("search-dropdown").value
    };
    var queryString = $.param(formData);
    $.ajax({
      url: searchUrl + "?" + queryString,
      type: "GET",
      success: function(response){
        if (response["response"]===true){
          console.log("search success");
          const element = document.getElementById(tableUrl.slice(1, -1));

          if (element) {
            element.click();
          }
        }
        else {
          console.log("Failed");
          alert(response["response"]);
        }
      }
    });
    event.preventDefault();
  }

  function toggleRow(event) {
    id = event.target
      .closest("tr")
      .querySelectorAll("td")[1]
      .textContent.trim();
    if (selectedStudent.includes(id)) {
      for (index in [0, 1, 2, 3, 4, 5, 6, 7]) {
        id = event.target.closest("tr").querySelectorAll("td")[index];
        if(id){
          id.classList.add("bg-gray-400", "text-white");
          id.classList.remove("bg-gray-200", "bg-gray-100");
        }
        else index==7;
      }
    } else {
      for (index in [0, 1, 2, 3, 4, 5, 6, 7]) {
        id = event.target.closest("tr").querySelectorAll("td")[index];
        if(id){
          id.classList.remove("bg-gray-400", "text-white");
          id.classList.add(index % 2 ? "bg-gray-100" : "bg-gray-200");
        }
        else index==7;
      }
    }
  }

  function toggleAllRow() {
    const table = document.getElementById("table-form"); // Get the table by its ID
    const rows = table.getElementsByTagName("tr");
    if (selectedStudent.length > 0) {
      for (let i = 0; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName("td");

        for (let j = 0; j < cells.length; j++) {
          cells[j].classList.add("bg-gray-400", "text-white");
          cells[j].classList.remove(j % 2 ? "bg-gray-100" : "bg-gray-200");
        }
      }
    } else {
      for (let i = 0; i < rows.length; i++) {
        const cells = rows[i].getElementsByTagName("td");

        for (let j = 0; j < cells.length; j++) {
          cells[j].classList.remove("bg-gray-400", "text-white");
          cells[j].classList.add(j % 2 ? "bg-gray-100" : "bg-gray-200");
        }
      }
    }
  }

  function allCheckbox(event) {
    ifAllChecked = event.target.checked ? true : false;
    document.querySelectorAll(".row-checkbox").forEach(function (tab) {
      tab.checked = ifAllChecked;
      if (
        ifAllChecked &&
        selectedStudent.indexOf(
          tab.closest("tr").querySelectorAll("td")[1].textContent.trim()
        )
      ) {
        selectedStudent.push(
          tab.closest("tr").querySelectorAll("td")[1].textContent.trim()
        );
      }
    });
    if (!ifAllChecked) selectedStudent = [];
    toggleAllRow();
    toggleDelete();
  }

  function toggleCheckBox(event) {
    const id = event.target
      .closest("tr")
      .querySelectorAll("td")[1]
      .textContent.trim();
    const index = selectedStudent.indexOf(id);
    if (index === -1) {
      selectedStudent.push(id);
    } else {
      selectedStudent.splice(index, 1);
    }
    toggleDelete();
    toggleRow(event);
  }

  function toggleDelete() {
    console.log("toggleDelete");
    const item = document.getElementById("delete_button");
    if (selectedStudent.length > 0) {
      item.disabled = false;
      item.classList.add(
        "bg-red-700",
        "border-red-700",
        "hover:bg-red-800",
        "focus:ring-4",
        "focus:outline-none",
        "focus:ring-red-300",
        "text-white"
      );
      item.classList.remove(
        "text-gray-200",
        "cursor-not-allowed",
        "bg-red-300",
        "border-red-300"
      );
    } else {
      item.disabled = true;
      item.classList.remove(
        "bg-red-700",
        "border-red-700",
        "hover:bg-red-800",
        "focus:ring-4",
        "focus:outline-none",
        "focus:ring-red-300",
        "text-white"
      );
      item.classList.add(
        "text-gray-200",
        "cursor-not-allowed",
        "bg-red-300",
        "border-red-300"
      );
    }
  }
  
    function closingDeleteDialog() {
      console.log("CLOSING DIALOG");
      const divToDelete = document.querySelector("[modal-backdrop]");
      if (divToDelete !== null) {
        document.getElementById("info-popup").classList.add("hidden");
        divToDelete.remove();
      }
    }

  function deleteStudentDialog() {
    console.log("deleteStudentDialog called");
    dialog = document.getElementById("info-popup");
    dialog.classList.remove("hidden");
    dialog.classList.add("flex");
    dialog.setAttribute("role", "dialog");
    dialog.setAttribute("aria-modal", "true");

    const newDiv = document.createElement("div");

    // Customize the new div (e.g., add content, classes, styles)
    newDiv.setAttribute("modal-backdrop", "");
    newDiv.className =
      "bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-40";

    // Append the new div to the body of the document
    document.body.appendChild(newDiv);
  }

  function deleteCall(event) {
    console.log("tab @ deleteCall:" + tableUrl);
    deleteUrl = tableUrl + "delete/";
    const csrfToken = document
      .querySelector("meta[name=csrf-token]")
      .getAttribute("content");
    const formData = {
      list: selectedStudent,
    };
    console.log("formData is " + JSON.stringify(formData, null, 2));

    $.ajax({
      type: "POST",
      url: deleteUrl,
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      data: JSON.stringify(formData),
      success: function(data) {
        console.log("before if-else");
        console.log(data);
        if(data['response']===true){
          const element = document.getElementById(tableUrl.slice(1, -1));
          if (element) {
            element.click();
          }
          alert(tableUrl.slice(1, -2)+ ((selectedStudent.length>1) ? "s have" : " has" )+" been deleted");
        }
        else alert(data["response"]);
      }});

    event.preventDefault();
  }

  function formDropdown(){
    console.log("formDropdown clicked");
    var formDropdownBlocks = document.getElementById("formDropdownBox");
    //var submit_button = document.getElementById("submit_button");
    if (formDropdownBlocks.classList.contains("hidden")) {
      formDropdownBlocks.classList.remove("hidden");
      formDropdownBlocks.classList.add("block");
      //submit_button.classList.add("hidden");
    } else {
      formDropdownBlocks.classList.remove("block");
      formDropdownBlocks.classList.add("hidden");
      //submit_button.classList.remove("hidden");
    }
  }

  function formDropdownBlocksClickHandler(event) {
    console.log("dropdown chose");
    if (event.target.tagName === "BUTTON") {
      console.log("valid");
      var dropdownButton = document.getElementById("formDropdownButton");
      var textNode = Array.from(dropdownButton.childNodes).find(function (
        node
      ) {
        return node.nodeType === 3; // Filter text nodes
      });
      textNode.replaceWith(event.target.textContent);
    }
  }

  

  function tablePick() {
    console.log("tablePick function executed");


    // Add event listeners for the dropdown functionality
    document
      .getElementById("dropdown-button")
      .addEventListener("click", toggleDropdown);

    document.addEventListener("click", documentClickHandler);

    document
      .getElementById("header-checkbox")
      .addEventListener("click", allCheckbox);

    const checkboxes = document.getElementsByClassName("row-checkbox");

    for (let i = 0; i < checkboxes.length; i++) {
      checkboxes[i].addEventListener("click", toggleCheckBox);
    }

    document
      .getElementById("dropdown-blocks")
      .addEventListener("click", dropdownBlocksClickHandler);

    document
      .getElementById("delete_button")
      .addEventListener("click", deleteStudentDialog);
    document
          .getElementById("searchbar-form")
          .addEventListener("submit", searchTable);

    document
      .getElementById("proceed-to-delete")
      .addEventListener("click", deleteCall);

    document
      .querySelectorAll(".remove-custom-backdrop")
      .forEach(function (tab) {
        if ($(this).attr("id") != "proceed-to-delete")
          tab.addEventListener("click", closingDeleteDialog);
      });

    //GET for searchbar and table
    document.getElementById("add_entry").addEventListener("click", function () {
      var addUrl = tableUrl + "/add/";
      var content = document.getElementById("content");

      $(content).load(addUrl, function(){
        addEntry("add");
      });

    });

    document.querySelector("table").addEventListener("click", function (event) {
      if (event.target.classList.contains("edit-btn")) {
        var editUrl = tableUrl + "edit/";
        var content = document.getElementById("content");

        const leftmostData = event.target
          .closest("tr")
          .querySelectorAll("td")[1]
          .textContent.trim();
        console.log("leftmostData:");
        console.log(leftmostData);

        var csrf_token = "{{ csrf_token() }}";
        var formData = {}
        if(tableUrl=="/students/"){
          formData = {
            id: leftmostData
          };
        }
        else if(tableUrl=="/courses/" || tableUrl=="/colleges/"){
          formData = {
            code: leftmostData
          };
        }
        var queryString = $.param(formData);
        console.log("formData is " + JSON.stringify(formData, null, 2));
        $(content).load(editUrl+"?"+queryString,function(){
          addEntry("edit");
        });
        event.preventDefault();
      }
    });
  }

  function addEntry(type) {
    url = tableUrl+ ((type == "add") ?  "add" : "edit") +tableUrl.slice(1, -2)+"/"; 
    console.log("addEntry function executed");

    if($("#id").length > 0){// /students/
      const input = document.getElementById("id");
    }
      console.log("formDropdownBox exists");

      if ($("#formDropdownButton").length > 0)
        document
          .getElementById("formDropdownButton")
          .addEventListener("click", formDropdown);
      
      if ($("#formDropdownBox-choices").length > 0)
      document
        .getElementById("formDropdownBox-choices")
        .addEventListener("click", formDropdownBlocksClickHandler);

      function previewFile() {
        console.log("PREVIEW PRESSED")
        var preview = document.getElementById('profile-image');
        var file    = document.getElementById('profile-image-upload').files[0];
        var reader  = new FileReader();
      
        if (file) {
          reader.readAsDataURL(file);
        }
      
        reader.addEventListener("load", function () {
          preview.style.height = '150px';
          preview.style.width = '150px';
          preview.style.objectFit = 'cover';
          preview.src = reader.result;

          document.getElementById("delete-image").classList.remove("cursor-not-allowed");
          document.getElementById("delete-image").classList.add("cursor-pointer");
        }, false);
      }
      
      document
        .getElementById("upload-image")
        .addEventListener("click", function() {
            $('#profile-image-upload').click();
        });
      document
        .getElementById("profile-image-upload")
        .addEventListener("change", previewFile);

      document
        .getElementById("delete-image")
        .addEventListener("click", removeImage);

      function removeImage(){
        var file    = document.getElementById('profile-image-upload').files[0];
        var reader  = new FileReader();
      
        if (file) {
          reader.readAsDataURL(file);
          console.log("checking if there's a pic");
          // replace both profile-image-upload profile-image
          console.log("there's a pic to be removed");
          var newRemove = $("<input id='profile-image-upload' accept='image/*' class='hidden' type='file' multiple='false'>");
          var preview = document.getElementById('profile-image');

          //replace with default_pic
          preview.style.height = '150px';
          preview.style.width = '150px';
          preview.style.objectFit = 'cover';
          preview.src = 'static/default_pic.svg';
      
          // replace the old input with the new one
          $("#profile-image-upload").replaceWith(newRemove);
          
          document.getElementById("delete-image").classList.add("cursor-not-allowed");
          document.getElementById("delete-image").classList.remove("cursor-pointer");

          document
            .getElementById("upload-image")
            .addEventListener("click", function() {
                $('#profile-image-upload').click();
            });
          document
            .getElementById("profile-image-upload")
            .addEventListener("change", previewFile);
          console.log("DELETED");
        }
      }

    //}

    function formValidator(formData){
      toCheck = ("id" in formData) ? "id" : "code";
        $.ajax({
          url: tableUrl+"verify/"+formData[toCheck],
          type: "GET",
          success: function(response){
            if (response["response"]!==true){
              console.log("Failed");
              alert(response["response"]);
            }
            else {
              console.log("Add success");
              modifyDatabase(formData);
            }
          }
        });
      }

    function modifyDatabase(formData){
      console.log("Success")
      console.log("formData is " + JSON.stringify(formData, null, 2));
      $.ajax({
        type: "POST",
        url: url,
        data: JSON.stringify(formData),
        contentType: "application/json", // Set the content type to JSON
        headers: {
          "X-CSRFToken": $('meta[name=csrf-token]').attr('content')
        },
        success: function(response) {
          if(response["response"]===true){
            console.log("POST SUCCESSFUL");
            var element = document.getElementById(tableUrl.slice(1, -1));

            if(tableUrl == "/students/"){
              console.log("loading removed");
              $('.loading').remove();
            }

            // Check if the element exists (not null)
            if (element) {
              // Programmatically trigger a click event
              $(element).click();
              alert(tableUrl.slice(1, -2)+" has been successfully "+type+"ed");
            }
          }
          else{
            alert(response["response"]);
          }
        },
      });
    }


    document
      .getElementById("add-edit-form")
      .addEventListener("submit", function (event) {
        console.log("POST");
        var csrf_token = "{{ csrf_token() }}";

        var formData = {};
        if (tableUrl=="/students/"){
          $.ajax({
              url: tableUrl+'loading',  // Replace with your Flask route
              method: 'GET',
              success: function(data) {
                  // Append the dynamic content to the modal
                  console.log("modal appended")
                  $('#modal').append(data);
              },
              error: function(error) {
                  console.error('Error fetching dynamic content:', error);
              }
          });
          formData = {
            profile_pic: document.getElementById('profile-image').getAttribute('src'),
            id: $("#id").val().trim(),
            firstname: $("#firstname").val(),
            lastname: $("#lastname").val(),
            year: $("#year").val(),
            gender: $("#gender").val(),
          };
          formData["course"] = $("#formDropdownButton").contents().filter(function() {            
                  return this.nodeType === 3; // Filter text nodes
              }).text().trim();
        }
        else{
          formData = {
            code: $("#code").val().trim(),
            name: $("#name").val(),
          }
          if (tableUrl=="/courses/"){
            formData["college"] = $("#formDropdownButton").contents().filter(function() {            
                  return this.nodeType === 3; // Filter text nodes
              }).text().trim()
          }
        }
        console.log(formData)
        if (type=="add") formValidator(formData);
        else modifyDatabase(formData);
        event.preventDefault();
      });
  }

  // Add event listeners to .btn-tabs elements
  document.querySelectorAll(".btn-tabs").forEach(function (tab) {
    tab.addEventListener("click", handleTabClick);
  });

  $(document).ready(function () {
    document.getElementById("students").click();
  });