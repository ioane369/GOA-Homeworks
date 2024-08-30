// Do two 6 kyu katas from Codewars using JavaScript.

// 1) IP Validation
function isValidIP(str){
    if (/[a-zA-Z]/.test(str)){
      return false;
    }
    
    const octets = str.split('.');
    if (octets.length != 4){
      return false;
    }
    
    for (const value of octets){
      const num = Number(value);
      if (isNaN(num) || String(num) !== value || num < 0 || num > 255){
        return false;
      }
    }
    return true;
}

console.log(isValidIP("137.255.156.100"));
console.log(isValidIP('1e0.1e1.1e2.2e2'));



// 2) Title Case
function titleCase(title, minorWords){ 
    if (title === ''){
      return '';
    }
    
    function capitalize(word){
      return word[0].toUpperCase() + word.slice(1)
    }
    
    const words = title.toLowerCase().split(' ');
    const res = [capitalize(words[0])];
    
    if (minorWords){
      minorWords = minorWords.toLowerCase().split(' ')
      for (let word of words.slice(1)){
        if (minorWords.includes(word)){
          res.push(word);
        } else {
          res.push(capitalize(word));
        }
      }
    } else {
      for (let word of words.slice(1)){
        res.push(capitalize(word));
      }
    }
    return res.join(' ');
}

console.log(titleCase('a clash of KINGS', 'a an the of'));