use std::collections::HashMap;

pub fn suma(left: f64, right: f64) -> f64{
    left + right
}

pub fn resta(left: f64, right: f64) -> f64{
    left - right
}

pub fn miltiplicar(left: f64, right: f64) -> f64{
    left * right
}

pub fn factorial(left: u64) -> f64{
    let mut count: u64 = 0;
    let mut a1: f64 = 1.0;
    while count < left {
        count += 1;
        a1 *= count as f64;
    }
    a1
}


pub fn promedio(vector: &[f64]) -> f64{
    let mut suma: f64 = vector.iter().sum::<f64>();
    let mut longitud: f64 =vector.len() as f64;
    let mut promedio: f64  = (suma as f64) / longitud;
    promedio
}

pub fn mediana(vector: &mut Vec<f64>) -> f64{
    let mut longitud: f64 = (vector.len() as f64 / 2.0).round() as f64;
    vector.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let mut resultado: f64 = vector[longitud as usize-1] as f64;
        resultado
}

pub fn moda(vector: &[f64]) -> f64 {
    let mut frecuencias = HashMap::new();

    for &elemento in vector {
        *frecuencias.entry(elemento.to_bits() as i64).or_insert(0) += 1;
    }

    let mut moda = vector[0];
    let mut frecuencia_maxima = 0;

    for (&elemento, &frecuencia) in &frecuencias {
        if frecuencia > frecuencia_maxima {
            moda = f64::from_bits(elemento as u64);
            frecuencia_maxima = frecuencia;
        }
    }

    moda
}

pub fn varianza(vector: &[f64]) -> f64 {
    let mut longitud: f64 = promedio(&vector);
    let mut a: u64 = 0;
    let mut b: f64 = 0.0;
    let mut c: f64 = 0.0;
    for &elemento in vector {
        if a==0{
            b = (elemento as f64 - longitud).powi(2);
    }else{
        b = b + (elemento as f64 - longitud).powi(2);
    }
    a = a + 1;
    }
    c=b/vector.len() as f64;
    c as f64
}

pub fn desviacion(vector: &[f64]) -> f64 {
    let mut longitud: f64 = varianza(&vector);
    let a: f64 = (longitud as f64).sqrt();
    a as f64
}

pub fn producto_escalar(vector1: &[f64], vector2: &[f64]) -> f64 {
    vector1.iter().zip(vector2.iter()).map(|(x, y)| x * y).sum()
}

pub fn peso(vector: &[f64],vector2: &[f64]) -> f64 {
    let mut resultado = producto_escalar(&vector, &vector2);
    let mut suma: f64 = 0.0;
    for &elemento in vector2 {
        suma += elemento;
    }
    let mut resultado2 = resultado/suma;
    resultado2
}