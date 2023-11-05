export function getPriceKey(cabinType) {
  return cabinType === 'Class' ? 'first_class_price' : `${(cabinType || '').toLowerCase()}_price`
}