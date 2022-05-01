const form = document.getElementById("form");
const inputFile = document.getElementById("file");

const handleSubmit = async (event) => {
    event.preventDefault()

    const body = {
        image1: document.getElementById("image1").value,
        image2: document.getElementById("image2").value,
        image3: document.getElementById("image3").value,
        image4: document.getElementById("image4").value,
        bathroom: document.getElementById("bathroom").value,
        bedrooms: document.getElementById("bedrooms").value,
        meters: document.getElementById("meters").value,
        zip: document.getElementById("zip").value,
    }

    const response = await fetch('http://127.0.0.1:5000/results', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify(body)
      });
      
    const scores = await response.json();
    console.log(scores)
    


    // window.open("./results.html")

    document.location.href = "./results";
    localStorage.scores=getElementById("scores")
   
   


};

form.addEventListener("submit", handleSubmit);



// async function imageToBase64(imageBlob) {
//     return new Promise((resolve, reject) => {
//         const reader = new FileReader()
//         reader.onloadend = () => resolve(reader.result)
//         reader.onerror = reject
//         reader.readAsDataURL(imageBlob)
//     })
// }