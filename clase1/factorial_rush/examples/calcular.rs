use factorial_rush;

fn main() {
    println!("la suma es: {}", factorial_rush::suma(2.1, 3.1));
    println!("factorial: {}", factorial_rush::factorial(5));
    let mut vector = vec![1, 2,3,4,5];
    let mut vector1 = vec![1, 2,3,4,5];
    let mut vector_f64: Vec<f64> = vector.iter().map(|&x| x as f64).collect();
    let mut vector_f641: Vec<f64> = vector1.iter().map(|&x| x as f64).collect();
    println!("promedio: {}", factorial_rush::promedio(&vector_f64));
    println!("mediana: {}", factorial_rush::mediana(&mut vector_f64));
    println!("moda: {}", factorial_rush::moda(&mut vector_f64));
    println!("varianza: {}", factorial_rush::varianza(&mut vector_f64));
    
    println!("desviacion: {}", factorial_rush::desviacion(&vector_f64));
    println!("peso: {}", factorial_rush::peso(&mut vector_f64, &mut vector_f641));
}