﻿namespace Persistence.Data.Configurations
{
    internal class ProductConfigurations : IEntityTypeConfiguration<Product>
    {
        public void Configure(EntityTypeBuilder<Product> builder)
        {
            builder.HasOne(product => product.ProductBrand)
                .WithMany()
                .HasForeignKey(product => product.BrandId);


            builder.HasOne(product => product.ProductType)
                .WithMany()
                .HasForeignKey(product => product.TypeId);

            builder.Property(product => product.Price)
                .HasColumnType("decimal(18,5)");

            builder.Property(product => product.PictureUrl)
                .HasDefaultValue("null");
        }
    }
}
